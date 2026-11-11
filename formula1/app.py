"""
app.py
------
Aplicação Flask do Portal 'Setor F1'.
- Zero ORM: consultas diretas com cursor nativo (psycopg2).
- Autenticação com senhas criptografadas (werkzeug.security).
- Perfil de Administrador:
  * Publicação e EDIÇÃO de notícias
  * Cadastro e EDIÇÃO de corridas (com Pole Position, Pódio 1º/2º/3º, Volta Rápida e Classificação)
  * Cadastro e EDIÇÃO de pilotos (titulares e reservas, com upload de fotos)
  * Cadastro e EDIÇÃO de equipes (carros, motores e gestão de pilotos)
  * Cadastro e EDIÇÃO de produtos da loja com tags e banners rotativos
  * Gestão de fotos da galeria
- Loja Oficial com Carrossel de Produtos e fluxo seguro de compra
- Página de Detalhes da Corrida (/corrida/<id>) com classificação e informações completas
- Galeria de Fotos integrada sem sobrecarregar o menu principal
"""

import os
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from db import get_db_connection

# Carrega variáveis de ambiente
load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "setorf1_super_secret_dev_key")

UPLOAD_PRODUTOS = os.path.join(app.root_path, "static", "images", "produtos")
UPLOAD_PILOTOS = os.path.join(app.root_path, "static", "images", "pilotos")
UPLOAD_GALERIA = os.path.join(app.root_path, "static", "images", "galeria")
for p in [UPLOAD_PRODUTOS, UPLOAD_PILOTOS, UPLOAD_GALERIA]:
    os.makedirs(p, exist_ok=True)

# Mapeamento auxiliar de bandeiras em emoji
EMOJIS_BANDEIRAS = {
    "br": "🇧🇷", "at": "🇦🇹", "us": "🇺🇸", "qa": "🇶🇦",
    "ae": "🇦🇪", "au": "🇦🇺", "gb": "🇬🇧", "mc": "🇲🇨",
    "nl": "🇳🇱", "es": "🇪🇸", "fi": "🇫🇮", "de": "🇩🇪",
    "it": "🇮🇹", "fr": "🇫🇷", "mx": "🇲🇽", "jp": "🇯🇵",
    "ca": "🇨🇦", "be": "🇧🇪", "hu": "🇭🇺", "az": "🇦🇿",
    "nz": "🇳🇿"
}

@app.template_filter("bandeira")
def filtro_bandeira(codigo):
    if not codigo:
        return "🏁"
    return EMOJIS_BANDEIRAS.get(codigo.lower().strip(), "🏁")


# ==============================================================================
# DECORADORES DE CONTROLE DE ACESSO
# ==============================================================================
def login_necessario(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Por favor, faça login para continuar.", "info")
            return redirect(url_for("login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function


def admin_necessario(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "usuario_id" not in session or session.get("usuario_tipo") != "admin":
            flash("Acesso restrito para administradores do Setor F1.", "error")
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return decorated_function


# ==============================================================================
# ROTA 1: PÁGINA INICIAL (BANNERS ROTATIVOS + NOTÍCIAS + DATATABLE DE PILOTOS)
# ==============================================================================
@app.route("/")
def index():
    conn = get_db_connection()
    cur = conn.cursor()

    # 1. Banners da Home
    cur.execute("""
        SELECT * FROM banners 
        WHERE ativo = TRUE AND local_exibicao = 'home'
        ORDER BY ordem ASC, id DESC;
    """)
    banners = cur.fetchall()

    # 2. DataTable dos Pilotos da Temporada
    cur.execute("""
        SELECT 
            p.*, 
            e.nome AS equipe_nome, 
            e.cor_primaria,
            e.logo_url AS equipe_logo
        FROM pilotos p
        LEFT JOIN equipes e ON p.equipe_id = e.id
        WHERE p.ativo = TRUE
        ORDER BY p.pontos_temporada DESC, p.vitorias DESC, p.nome ASC;
    """)
    pilotos_tabela = cur.fetchall()

    # 3. Notícias recentes
    cur.execute("""
        SELECT * FROM noticias 
        ORDER BY destaque DESC, data_publicacao DESC 
        LIMIT 6;
    """)
    noticias = cur.fetchall()

    # 4. Próxima corrida
    cur.execute("""
        SELECT * FROM corridas 
        WHERE status = 'proxima' 
        ORDER BY data_corrida ASC 
        LIMIT 1;
    """)
    proxima_corrida = cur.fetchone()

    cur.close()
    conn.close()

    return render_template(
        "index.html",
        banners=banners,
        pilotos_tabela=pilotos_tabela,
        noticias=noticias,
        proxima_corrida=proxima_corrida
    )


# ==============================================================================
# ROTA 1.1: DETALHE DA NOTÍCIA
# ==============================================================================
@app.route("/noticia/<int:id>")
def noticia_detalhe(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM noticias WHERE id = %s;", (id,))
    noticia = cur.fetchone()

    cur.close()
    conn.close()

    if not noticia:
        flash("Notícia não encontrada.", "error")
        return redirect(url_for("index"))

    return render_template("noticia_detalhe.html", noticia=noticia)


# ==============================================================================
# ROTA 2: PÁGINA DE PILOTOS (ATUAIS E HISTÓRICOS COM BUSCA)
# ==============================================================================
@app.route("/pilotos")
def pilotos():
    termo_busca = request.args.get("busca", "").strip()
    filtro_status = request.args.get("status", "todos").strip()

    conn = get_db_connection()
    cur = conn.cursor()

    query = """
        SELECT 
            p.*, 
            e.nome AS equipe_nome, 
            e.cor_primaria, 
            e.logo_url AS equipe_logo
        FROM pilotos p
        LEFT JOIN equipes e ON p.equipe_id = e.id
        WHERE 1=1
    """
    params = []

    if termo_busca:
        query += " AND (p.nome ILIKE %s OR p.nacionalidade ILIKE %s OR e.nome ILIKE %s)"
        like_termo = f"%{termo_busca}%"
        params.extend([like_termo, like_termo, like_termo])

    if filtro_status == "atual":
        query += " AND p.ativo = TRUE"
    elif filtro_status == "historico":
        query += " AND p.ativo = FALSE"

    query += " ORDER BY p.ativo DESC, p.pontos_temporada DESC, p.titulos_mundiais DESC, p.nome ASC;"

    cur.execute(query, tuple(params))
    lista_pilotos = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        "pilotos.html",
        pilotos=lista_pilotos,
        termo_busca=termo_busca,
        filtro_status=filtro_status
    )


# ==============================================================================
# ROTA 2.1: PERFIL DO PILOTO
# ==============================================================================
@app.route("/piloto/<int:id>")
def piloto_detalhe(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            p.*, 
            e.nome AS equipe_nome, 
            e.cor_primaria,
            e.logo_url AS equipe_logo
        FROM pilotos p
        LEFT JOIN equipes e ON p.equipe_id = e.id
        WHERE p.id = %s;
    """, (id,))
    piloto = cur.fetchone()

    cur.close()
    conn.close()

    if not piloto:
        flash("Piloto não encontrado.", "error")
        return redirect(url_for("pilotos"))

    return render_template("piloto_detalhe.html", piloto=piloto)


# ==============================================================================
# ROTA 3: PÁGINA DE EQUIPES (COM PILOTOS TITULARES E RESERVAS)
# ==============================================================================
@app.route("/equipes")
def equipes():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM equipes ORDER BY titulos_construtores DESC, nome ASC;")
    lista_equipes = cur.fetchall()

    equipes_com_pilotos = []
    for equipe in lista_equipes:
        cur.execute("""
            SELECT id, nome, numero, foto_url, ativo, papel_equipe 
            FROM pilotos 
            WHERE equipe_id = %s 
            ORDER BY papel_equipe ASC, pontos_temporada DESC, numero ASC;
        """, (equipe["id"],))
        todos_pilotos = cur.fetchall()

        eq_dict = dict(equipe)
        eq_dict["titulares"] = [p for p in todos_pilotos if p["papel_equipe"] == "titular"]
        eq_dict["reservas"] = [p for p in todos_pilotos if p["papel_equipe"] == "reserva"]
        equipes_com_pilotos.append(eq_dict)

    cur.close()
    conn.close()

    return render_template("equipes.html", equipes=equipes_com_pilotos)


# ==============================================================================
# ROTA 4: PÁGINA DE CORRIDAS (HISTÓRICAS, RESULTADOS E PRÓXIMAS)
# ==============================================================================
@app.route("/corridas")
def corridas():
    ano_filtro = request.args.get("ano", "todos")

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT DISTINCT ano FROM corridas ORDER BY ano DESC;")
    anos_disponiveis = [r["ano"] for r in cur.fetchall()]

    query_concluidas = """
        SELECT 
            c.*, 
            p.nome AS vencedor_nome, 
            p.foto_url AS vencedor_foto
        FROM corridas c
        LEFT JOIN pilotos p ON c.vencedor_piloto_id = p.id
        WHERE c.status = 'concluida'
    """
    params_concluidas = []

    if ano_filtro != "todos" and ano_filtro.isdigit():
        query_concluidas += " AND c.ano = %s"
        params_concluidas.append(int(ano_filtro))

    query_concluidas += " ORDER BY c.ano DESC, c.data_corrida DESC;"
    cur.execute(query_concluidas, tuple(params_concluidas))
    corridas_concluidas = cur.fetchall()

    corrida_destaque = corridas_concluidas[0] if corridas_concluidas else None

    cur.execute("""
        SELECT * FROM corridas 
        WHERE status = 'proxima' 
        ORDER BY data_corrida ASC;
    """)
    proximas_corridas = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        "corridas.html",
        corridas_concluidas=corridas_concluidas,
        corrida_destaque=corrida_destaque,
        proximas_corridas=proximas_corridas,
        anos_disponiveis=anos_disponiveis,
        ano_selecionado=ano_filtro
    )


# ==============================================================================
# ROTA 4.1: INFORMAÇÕES COMPLETAS DA CORRIDA (POLE, PÓDIO E CLASSIFICAÇÃO)
# ==============================================================================
@app.route("/corrida/<int:id>")
def corrida_detalhe(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            c.*,
            p_venc.nome AS vencedor_nome, p_venc.foto_url AS vencedor_foto,
            p_seg.nome AS segundo_nome, p_seg.foto_url AS segundo_foto,
            p_terc.nome AS terceiro_nome, p_terc.foto_url AS terceiro_foto,
            p_pole.nome AS pole_nome, p_pole.foto_url AS pole_foto,
            p_volta.nome AS volta_nome, p_volta.foto_url AS volta_foto
        FROM corridas c
        LEFT JOIN pilotos p_venc ON c.vencedor_piloto_id = p_venc.id
        LEFT JOIN pilotos p_seg ON c.segundo_piloto_id = p_seg.id
        LEFT JOIN pilotos p_terc ON c.terceiro_piloto_id = p_terc.id
        LEFT JOIN pilotos p_pole ON c.pole_position_piloto_id = p_pole.id
        LEFT JOIN pilotos p_volta ON c.volta_rapida_piloto_id = p_volta.id
        WHERE c.id = %s;
    """, (id,))
    corrida = cur.fetchone()

    cur.close()
    conn.close()

    if not corrida:
        flash("Corrida não encontrada.", "error")
        return redirect(url_for("corridas"))

    return render_template("corrida_detalhe.html", corrida=corrida)


# ==============================================================================
# ROTA 5: LOJA OFICIAL SETOR F1 (COM CARROSSEL DE BANNERS DA LOJA)
# ==============================================================================
@app.route("/loja")
def loja():
    categoria_filtro = request.args.get("categoria", "todos")

    conn = get_db_connection()
    cur = conn.cursor()

    # Banners da Loja
    cur.execute("""
        SELECT * FROM banners 
        WHERE ativo = TRUE AND local_exibicao = 'loja'
        ORDER BY ordem ASC, id DESC;
    """)
    banners_loja = cur.fetchall()

    # Categorias
    cur.execute("SELECT DISTINCT categoria FROM produtos ORDER BY categoria ASC;")
    categorias = [c["categoria"] for c in cur.fetchall()]

    query = """
        SELECT p.*, e.nome AS equipe_nome, e.cor_primaria 
        FROM produtos p
        LEFT JOIN equipes e ON p.equipe_id = e.id
        WHERE 1=1
    """
    params = []

    if categoria_filtro != "todos":
        query += " AND p.categoria = %s"
        params.append(categoria_filtro)

    query += " ORDER BY p.destaque DESC, p.id DESC;"
    cur.execute(query, tuple(params))
    produtos = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        "loja.html",
        banners_loja=banners_loja,
        produtos=produtos,
        categorias=categorias,
        categoria_selecionada=categoria_filtro
    )


# ==============================================================================
# ROTA 5.1: COMPRA DE PRODUTO
# ==============================================================================
@app.route("/comprar/<int:produto_id>", methods=["POST"])
def comprar(produto_id):
    if "usuario_id" not in session:
        flash("Para adquirir itens na Loja Setor F1, faça seu cadastro de fã ou entre com sua conta!", "info")
        return redirect(url_for("cadastro", next=url_for("loja")))

    usuario_id = session["usuario_id"]
    quantidade = int(request.form.get("quantidade", 1))

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM produtos WHERE id = %s;", (produto_id,))
    produto = cur.fetchone()

    if not produto or produto["estoque"] < quantidade:
        flash("Produto indisponível ou estoque insuficiente.", "error")
        cur.close()
        conn.close()
        return redirect(url_for("loja"))

    valor_total = float(produto["preco"]) * quantidade

    cur.execute("""
        INSERT INTO pedidos (usuario_id, produto_id, quantidade, valor_total, status, endereco_entrega)
        VALUES (%s, %s, %s, %s, 'Confirmado', 'Endereço cadastrado na conta do fã');
    """, (usuario_id, produto_id, quantidade, valor_total))

    cur.execute("UPDATE produtos SET estoque = estoque - %s WHERE id = %s;", (quantidade, produto_id))

    conn.commit()
    cur.close()
    conn.close()

    flash(f"Compra realizada com sucesso! Pedido de {quantidade}x '{produto['nome']}' confirmado.", "success")
    return redirect(url_for("meus_pedidos"))


# ==============================================================================
# ROTA 5.2: MEUS PEDIDOS
# ==============================================================================
@app.route("/meus-pedidos")
@login_necessario
def meus_pedidos():
    usuario_id = session["usuario_id"]

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            ped.*, 
            prod.nome AS produto_nome, 
            prod.imagem_url AS produto_imagem,
            prod.categoria AS produto_categoria,
            prod.tag AS produto_tag
        FROM pedidos ped
        JOIN produtos prod ON ped.produto_id = prod.id
        WHERE ped.usuario_id = %s
        ORDER BY ped.data_pedido DESC;
    """, (usuario_id,))
    pedidos = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("meus_pedidos.html", pedidos=pedidos)


# ==============================================================================
# ROTA 6: GALERIA DE FOTOS (FOTOS EM ALTA DEFINIÇÃO DO PADDOCK)
# ==============================================================================
@app.route("/galeria")
def galeria():
    categoria = request.args.get("cat", "todos")

    conn = get_db_connection()
    cur = conn.cursor()

    query = "SELECT * FROM galeria"
    params = []
    if categoria != "todos":
        query += " WHERE categoria = %s"
        params.append(categoria)
    query += " ORDER BY id DESC;"

    cur.execute(query, tuple(params))
    fotos = cur.fetchall()

    cur.execute("SELECT DISTINCT categoria FROM galeria ORDER BY categoria ASC;")
    categorias = [c["categoria"] for c in cur.fetchall()]

    cur.close()
    conn.close()

    return render_template("galeria.html", fotos=fotos, categorias=categorias, categoria_atual=categoria)


# ==============================================================================
# ROTA 7: AUTENTICAÇÃO (CADASTRO, LOGIN E LOGOUT)
# ==============================================================================
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")
        next_url = request.args.get("next") or url_for("loja")

        if not (nome and email and senha):
            flash("Preencha todos os campos para criar sua conta.", "error")
            return redirect(url_for("cadastro"))

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT id FROM usuarios WHERE email = %s;", (email,))
        if cur.fetchone():
            flash("Este e-mail já está cadastrado. Faça login!", "error")
            cur.close()
            conn.close()
            return redirect(url_for("login"))

        senha_hash = generate_password_hash(senha)
        cur.execute("""
            INSERT INTO usuarios (nome, email, senha_hash, tipo)
            VALUES (%s, %s, %s, 'cliente')
            RETURNING id;
        """, (nome, email, senha_hash))
        novo_id = cur.fetchone()["id"]
        conn.commit()

        cur.close()
        conn.close()

        session["usuario_id"] = novo_id
        session["usuario_nome"] = nome
        session["usuario_email"] = email
        session["usuario_tipo"] = "cliente"

        flash(f"Bem-vindo(a) ao Setor F1, {nome}! Sua conta foi criada com sucesso.", "success")
        return redirect(next_url)

    return render_template("cadastro.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")
        next_url = request.args.get("next")

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM usuarios WHERE email = %s;", (email,))
        usuario = cur.fetchone()

        cur.close()
        conn.close()

        if usuario and check_password_hash(usuario["senha_hash"], senha):
            session["usuario_id"] = usuario["id"]
            session["usuario_nome"] = usuario["nome"]
            session["usuario_email"] = usuario["email"]
            session["usuario_tipo"] = usuario["tipo"]

            flash(f"Olá, {usuario['nome']}! Login realizado com sucesso.", "success")

            if usuario["tipo"] == "admin":
                return redirect(url_for("admin_dashboard"))
            
            return redirect(next_url or url_for("index"))
        else:
            flash("E-mail ou senha incorretos. Tente novamente.", "error")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("Você saiu da sua conta.", "info")
    return redirect(url_for("index"))


# ==============================================================================
# ROTA 8: ÁREA ADMINISTRATIVA DO SETOR F1 (/admin)
# ==============================================================================
@app.route("/admin")
@admin_necessario
def admin_dashboard():
    conn = get_db_connection()
    cur = conn.cursor()

    # Métricas gerais
    cur.execute("SELECT COUNT(*) AS total FROM noticias;")
    total_noticias = cur.fetchone()["total"]

    cur.execute("SELECT COUNT(*) AS total FROM corridas;")
    total_corridas = cur.fetchone()["total"]

    cur.execute("SELECT COUNT(*) AS total FROM pilotos;")
    total_pilotos = cur.fetchone()["total"]

    cur.execute("SELECT COUNT(*) AS total FROM equipes;")
    total_equipes = cur.fetchone()["total"]

    cur.execute("SELECT COUNT(*) AS total FROM produtos;")
    total_produtos = cur.fetchone()["total"]

    cur.execute("SELECT COUNT(*) AS total FROM galeria;")
    total_galeria = cur.fetchone()["total"]

    # Listagens
    cur.execute("SELECT * FROM noticias ORDER BY data_publicacao DESC;")
    todas_noticias = cur.fetchall()

    cur.execute("SELECT * FROM corridas ORDER BY ano DESC, data_corrida DESC;")
    todas_corridas = cur.fetchall()

    cur.execute("""
        SELECT p.*, e.nome AS equipe_nome 
        FROM pilotos p 
        LEFT JOIN equipes e ON p.equipe_id = e.id 
        ORDER BY p.ativo DESC, p.pontos_temporada DESC;
    """)
    todos_pilotos = cur.fetchall()

    cur.execute("SELECT * FROM equipes ORDER BY titulos_construtores DESC;")
    todas_equipes = cur.fetchall()

    cur.execute("""
        SELECT p.*, e.nome AS equipe_nome 
        FROM produtos p 
        LEFT JOIN equipes e ON p.equipe_id = e.id 
        ORDER BY p.id DESC;
    """)
    todos_produtos = cur.fetchall()

    cur.execute("SELECT * FROM banners ORDER BY local_exibicao ASC, ordem ASC, id DESC;")
    todos_banners = cur.fetchall()

    cur.execute("SELECT * FROM galeria ORDER BY id DESC;")
    todas_fotos = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        "admin.html",
        total_noticias=total_noticias,
        total_corridas=total_corridas,
        total_pilotos=total_pilotos,
        total_equipes=total_equipes,
        total_produtos=total_produtos,
        total_galeria=total_galeria,
        noticias=todas_noticias,
        corridas=todas_corridas,
        pilotos=todos_pilotos,
        equipes=todas_equipes,
        produtos=todos_produtos,
        banners=todos_banners,
        galeria=todas_fotos
    )


# ------------------------------------------------------------------------------
# ADMIN: GERENCIAMENTO DE PILOTOS (CRIAR, EDITAR, UPLOAD E EXCLUIR)
# ------------------------------------------------------------------------------
@app.route("/admin/piloto/criar", methods=["POST"])
@admin_necessario
def admin_criar_piloto():
    nome = request.form.get("nome", "").strip()
    numero = request.form.get("numero")
    numero = int(numero) if numero else None
    nacionalidade = request.form.get("nacionalidade", "").strip()
    pais_codigo = request.form.get("pais_codigo", "br").strip().lower()
    equipe_id = request.form.get("equipe_id")
    equipe_id = int(equipe_id) if equipe_id else None
    papel_equipe = request.form.get("papel_equipe", "titular")
    ativo = True if request.form.get("ativo") else False
    pontos_temporada = int(request.form.get("pontos_temporada", 0))
    chance_titulo = float(request.form.get("chance_titulo", 0.0))
    titulos_mundiais = int(request.form.get("titulos_mundiais", 0))
    vitorias = int(request.form.get("vitorias", 0))
    podios = int(request.form.get("podios", 0))
    como_entrou_f1 = request.form.get("como_entrou_f1", "").strip()
    trajetoria_f1 = request.form.get("trajetoria_f1", "").strip()

    imagem_url = request.form.get("foto_url", "").strip()
    foto_arquivo = request.files.get("foto_arquivo")

    if foto_arquivo and foto_arquivo.filename:
        nome_seguro = secure_filename(foto_arquivo.filename)
        caminho_salvar = os.path.join(UPLOAD_PILOTOS, nome_seguro)
        foto_arquivo.save(caminho_salvar)
        imagem_url = f"/static/images/pilotos/{nome_seguro}"
    elif not imagem_url:
        imagem_url = "https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO pilotos (nome, numero, nacionalidade, pais_codigo, equipe_id, foto_url,
                             como_entrou_f1, trajetoria_f1, titulos_mundiais, vitorias, podios,
                             ativo, papel_equipe, pontos_temporada, chance_titulo)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, (nome, numero, nacionalidade, pais_codigo, equipe_id, imagem_url,
          como_entrou_f1, trajetoria_f1, titulos_mundiais, vitorias, podios,
          ativo, papel_equipe, pontos_temporada, chance_titulo))

    conn.commit()
    cur.close()
    conn.close()

    flash(f"Piloto '{nome}' cadastrado com sucesso! Ele já pode ser escolhido em corridas e equipes.", "success")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/piloto/editar/<int:id>", methods=["GET", "POST"])
@admin_necessario
def admin_editar_piloto(id):
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        numero = request.form.get("numero")
        numero = int(numero) if numero else None
        nacionalidade = request.form.get("nacionalidade", "").strip()
        pais_codigo = request.form.get("pais_codigo", "br").strip().lower()
        equipe_id = request.form.get("equipe_id")
        equipe_id = int(equipe_id) if equipe_id else None
        papel_equipe = request.form.get("papel_equipe", "titular")
        ativo = True if request.form.get("ativo") else False
        pontos_temporada = int(request.form.get("pontos_temporada", 0))
        chance_titulo = float(request.form.get("chance_titulo", 0.0))
        titulos_mundiais = int(request.form.get("titulos_mundiais", 0))
        vitorias = int(request.form.get("vitorias", 0))
        podios = int(request.form.get("podios", 0))
        como_entrou_f1 = request.form.get("como_entrou_f1", "").strip()
        trajetoria_f1 = request.form.get("trajetoria_f1", "").strip()

        imagem_url = request.form.get("foto_url", "").strip()
        foto_arquivo = request.files.get("foto_arquivo")

        if foto_arquivo and foto_arquivo.filename:
            nome_seguro = secure_filename(foto_arquivo.filename)
            caminho_salvar = os.path.join(UPLOAD_PILOTOS, nome_seguro)
            foto_arquivo.save(caminho_salvar)
            imagem_url = f"/static/images/pilotos/{nome_seguro}"

        cur.execute("""
            UPDATE pilotos 
            SET nome = %s, numero = %s, nacionalidade = %s, pais_codigo = %s, equipe_id = %s,
                foto_url = COALESCE(NULLIF(%s, ''), foto_url),
                como_entrou_f1 = %s, trajetoria_f1 = %s, titulos_mundiais = %s, vitorias = %s, podios = %s,
                ativo = %s, papel_equipe = %s, pontos_temporada = %s, chance_titulo = %s
            WHERE id = %s;
        """, (nome, numero, nacionalidade, pais_codigo, equipe_id, imagem_url,
              como_entrou_f1, trajetoria_f1, titulos_mundiais, vitorias, podios,
              ativo, papel_equipe, pontos_temporada, chance_titulo, id))

        conn.commit()
        cur.close()
        conn.close()

        flash(f"Piloto '{nome}' atualizado com sucesso!", "success")
        return redirect(url_for("admin_dashboard"))

    cur.execute("SELECT * FROM pilotos WHERE id = %s;", (id,))
    piloto = cur.fetchone()

    cur.execute("SELECT id, nome FROM equipes ORDER BY nome ASC;")
    equipes = cur.fetchall()

    cur.close()
    conn.close()

    if not piloto:
        flash("Piloto não encontrado.", "error")
        return redirect(url_for("admin_dashboard"))

    return render_template("admin_editar_piloto.html", piloto=piloto, equipes=equipes)


@app.route("/admin/piloto/excluir/<int:id>", methods=["POST"])
@admin_necessario
def admin_excluir_piloto(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM pilotos WHERE id = %s;", (id,))
    conn.commit()

    cur.close()
    conn.close()

    flash("Piloto removido com sucesso.", "info")
    return redirect(url_for("admin_dashboard"))


# ------------------------------------------------------------------------------
# ADMIN: GERENCIAMENTO DE EQUIPES (CRIAR E EDITAR)
# ------------------------------------------------------------------------------
@app.route("/admin/equipe/criar", methods=["POST"])
@admin_necessario
def admin_criar_equipe():
    nome = request.form.get("nome", "").strip()
    nome_completo = request.form.get("nome_completo", "").strip()
    pais_origem = request.form.get("pais_origem", "").strip()
    sede = request.form.get("sede", "").strip()
    chefe_equipe = request.form.get("chefe_equipe", "").strip()
    motor = request.form.get("motor", "").strip()
    titulos = int(request.form.get("titulos_construtores", 0))
    ano_estreia = request.form.get("ano_estreia")
    ano_estreia = int(ano_estreia) if ano_estreia else None
    historia = request.form.get("historia", "").strip()
    logo_url = request.form.get("logo_url", "").strip()
    carro_modelo = request.form.get("carro_modelo", "").strip()
    carro_imagem_url = request.form.get("carro_imagem_url", "").strip()
    cor_primaria = request.form.get("cor_primaria", "#E10600").strip()

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO equipes (nome, nome_completo, pais_origem, sede, chefe_equipe, motor,
                             titulos_construtores, ano_estreia, historia, logo_url,
                             carro_modelo, carro_imagem_url, cor_primaria)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, (nome, nome_completo, pais_origem, sede, chefe_equipe, motor,
          titulos, ano_estreia, historia, logo_url, carro_modelo, carro_imagem_url, cor_primaria))

    conn.commit()
    cur.close()
    conn.close()

    flash(f"Equipe '{nome}' cadastrada com sucesso!", "success")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/equipe/editar/<int:id>", methods=["GET", "POST"])
@admin_necessario
def admin_editar_equipe(id):
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        nome_completo = request.form.get("nome_completo", "").strip()
        pais_origem = request.form.get("pais_origem", "").strip()
        sede = request.form.get("sede", "").strip()
        chefe_equipe = request.form.get("chefe_equipe", "").strip()
        motor = request.form.get("motor", "").strip()
        titulos = int(request.form.get("titulos_construtores", 0))
        ano_estreia = request.form.get("ano_estreia")
        ano_estreia = int(ano_estreia) if ano_estreia else None
        historia = request.form.get("historia", "").strip()
        logo_url = request.form.get("logo_url", "").strip()
        carro_modelo = request.form.get("carro_modelo", "").strip()
        carro_imagem_url = request.form.get("carro_imagem_url", "").strip()
        cor_primaria = request.form.get("cor_primaria", "#E10600").strip()

        cur.execute("""
            UPDATE equipes 
            SET nome = %s, nome_completo = %s, pais_origem = %s, sede = %s, chefe_equipe = %s, motor = %s,
                titulos_construtores = %s, ano_estreia = %s, historia = %s, logo_url = %s,
                carro_modelo = %s, carro_imagem_url = %s, cor_primaria = %s
            WHERE id = %s;
        """, (nome, nome_completo, pais_origem, sede, chefe_equipe, motor,
              titulos, ano_estreia, historia, logo_url, carro_modelo, carro_imagem_url, cor_primaria, id))

        conn.commit()
        cur.close()
        conn.close()

        flash(f"Equipe '{nome}' atualizada com sucesso!", "success")
        return redirect(url_for("admin_dashboard"))

    cur.execute("SELECT * FROM equipes WHERE id = %s;", (id,))
    equipe = cur.fetchone()

    # Pilotos vinculados
    cur.execute("SELECT * FROM pilotos WHERE equipe_id = %s ORDER BY papel_equipe ASC, numero ASC;", (id,))
    pilotos_da_equipe = cur.fetchall()

    cur.close()
    conn.close()

    if not equipe:
        flash("Equipe não encontrada.", "error")
        return redirect(url_for("admin_dashboard"))

    return render_template("admin_editar_equipe.html", equipe=equipe, pilotos=pilotos_da_equipe)


# ------------------------------------------------------------------------------
# ADMIN: CORRIDAS (CRIAR, EDITAR COM POLE E PÓDIO)
# ------------------------------------------------------------------------------
@app.route("/admin/corrida/criar", methods=["POST"])
@admin_necessario
def admin_criar_corrida():
    ano = int(request.form.get("ano", 2026))
    rodada = int(request.form.get("rodada", 1))
    nome_gp = request.form.get("nome_gp", "").strip()
    circuito = request.form.get("circuito", "").strip()
    pais = request.form.get("pais", "").strip()
    pais_codigo = request.form.get("pais_codigo", "br").strip().lower()
    cidade = request.form.get("cidade", "").strip()
    data_corrida = request.form.get("data_corrida")
    status = request.form.get("status", "proxima")

    pole_piloto_id = request.form.get("pole_position_piloto_id") or None
    pole_tempo = request.form.get("pole_position_tempo", "").strip()

    vencedor_id = request.form.get("vencedor_piloto_id") or None
    vencedor_equipe = request.form.get("vencedor_equipe", "").strip() or None

    segundo_id = request.form.get("segundo_piloto_id") or None
    segundo_lugar = request.form.get("segundo_lugar", "").strip() or None

    terceiro_id = request.form.get("terceiro_piloto_id") or None
    terceiro_lugar = request.form.get("terceiro_lugar", "").strip() or None

    volta_rapida_id = request.form.get("volta_rapida_piloto_id") or None
    volta_mais_rapida = request.form.get("volta_mais_rapida", "").strip() or None

    noticias_resumo = request.form.get("noticias_resumo", "").strip()
    classificacao = request.form.get("classificacao_detalhada", "").strip()

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO corridas (ano, rodada, nome_gp, circuito, pais, pais_codigo, cidade, data_corrida, status,
                              pole_position_piloto_id, pole_position_tempo,
                              vencedor_piloto_id, vencedor_equipe,
                              segundo_piloto_id, segundo_lugar,
                              terceiro_piloto_id, terceiro_lugar,
                              volta_rapida_piloto_id, volta_mais_rapida,
                              noticias_resumo, classificacao_detalhada)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, (ano, rodada, nome_gp, circuito, pais, pais_codigo, cidade, data_corrida, status,
          pole_piloto_id, pole_tempo, vencedor_id, vencedor_equipe, segundo_id, segundo_lugar,
          terceiro_id, terceiro_lugar, volta_rapida_id, volta_mais_rapida, noticias_resumo, classificacao))

    conn.commit()
    cur.close()
    conn.close()

    flash("Corrida salva com sucesso!", "success")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/corrida/editar/<int:id>", methods=["GET", "POST"])
@admin_necessario
def admin_editar_corrida(id):
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == "POST":
        ano = int(request.form.get("ano", 2026))
        rodada = int(request.form.get("rodada", 1))
        nome_gp = request.form.get("nome_gp", "").strip()
        circuito = request.form.get("circuito", "").strip()
        pais = request.form.get("pais", "").strip()
        pais_codigo = request.form.get("pais_codigo", "br").strip().lower()
        cidade = request.form.get("cidade", "").strip()
        data_corrida = request.form.get("data_corrida")
        status = request.form.get("status", "proxima")

        pole_piloto_id = request.form.get("pole_position_piloto_id") or None
        pole_tempo = request.form.get("pole_position_tempo", "").strip()

        vencedor_id = request.form.get("vencedor_piloto_id") or None
        vencedor_equipe = request.form.get("vencedor_equipe", "").strip() or None

        segundo_id = request.form.get("segundo_piloto_id") or None
        segundo_lugar = request.form.get("segundo_lugar", "").strip() or None

        terceiro_id = request.form.get("terceiro_piloto_id") or None
        terceiro_lugar = request.form.get("terceiro_lugar", "").strip() or None

        volta_rapida_id = request.form.get("volta_rapida_piloto_id") or None
        volta_mais_rapida = request.form.get("volta_mais_rapida", "").strip() or None

        noticias_resumo = request.form.get("noticias_resumo", "").strip()
        classificacao = request.form.get("classificacao_detalhada", "").strip()

        cur.execute("""
            UPDATE corridas 
            SET ano = %s, rodada = %s, nome_gp = %s, circuito = %s, pais = %s, pais_codigo = %s, cidade = %s,
                data_corrida = %s, status = %s,
                pole_position_piloto_id = %s, pole_position_tempo = %s,
                vencedor_piloto_id = %s, vencedor_equipe = %s,
                segundo_piloto_id = %s, segundo_lugar = %s,
                terceiro_piloto_id = %s, terceiro_lugar = %s,
                volta_rapida_piloto_id = %s, volta_mais_rapida = %s,
                noticias_resumo = %s, classificacao_detalhada = %s
            WHERE id = %s;
        """, (ano, rodada, nome_gp, circuito, pais, pais_codigo, cidade, data_corrida, status,
              pole_piloto_id, pole_tempo, vencedor_id, vencedor_equipe, segundo_id, segundo_lugar,
              terceiro_id, terceiro_lugar, volta_rapida_id, volta_mais_rapida,
              noticias_resumo, classificacao, id))

        conn.commit()
        cur.close()
        conn.close()

        flash("Corrida e resultados atualizados com sucesso!", "success")
        return redirect(url_for("admin_dashboard"))

    cur.execute("SELECT * FROM corridas WHERE id = %s;", (id,))
    corrida = cur.fetchone()

    cur.execute("SELECT id, nome FROM pilotos ORDER BY nome ASC;")
    pilotos = cur.fetchall()

    cur.close()
    conn.close()

    if not corrida:
        flash("Corrida não encontrada.", "error")
        return redirect(url_for("admin_dashboard"))

    return render_template("admin_editar_corrida.html", corrida=corrida, pilotos=pilotos)


@app.route("/admin/corrida/excluir/<int:id>", methods=["POST"])
@admin_necessario
def admin_excluir_corrida(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM corridas WHERE id = %s;", (id,))
    conn.commit()

    cur.close()
    conn.close()

    flash("Corrida excluída com sucesso.", "info")
    return redirect(url_for("admin_dashboard"))


# ------------------------------------------------------------------------------
# ADMIN: NOTÍCIAS (CRIAR, EDITAR E EXCLUIR)
# ------------------------------------------------------------------------------
@app.route("/admin/noticia/criar", methods=["POST"])
@admin_necessario
def admin_criar_noticia():
    titulo = request.form.get("titulo", "").strip()
    subtitulo = request.form.get("subtitulo", "").strip()
    categoria = request.form.get("categoria", "Geral").strip()
    imagem_url = request.form.get("imagem_url", "").strip()
    conteudo = request.form.get("conteudo", "").strip()
    destaque = True if request.form.get("destaque") else False
    no_banner = True if request.form.get("no_banner") else False

    if not imagem_url:
        imagem_url = "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=1200&q=80"

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO noticias (titulo, subtitulo, categoria, imagem_url, conteudo, destaque, no_banner, autor, criado_por_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
    """, (titulo, subtitulo, categoria, imagem_url, conteudo, destaque, no_banner, session.get("usuario_nome", "Redação Setor F1"), session.get("usuario_id")))
    nova_noticia_id = cur.fetchone()["id"]

    if no_banner:
        cur.execute("""
            INSERT INTO banners (titulo, subtitulo, imagem_url, link_url, tag_destaque, local_exibicao)
            VALUES (%s, %s, %s, %s, %s, 'home');
        """, (titulo, subtitulo or "Confira a matéria completa no Setor F1", imagem_url, f"/noticia/{nova_noticia_id}", f"NOTÍCIA: {categoria.upper()}"))

    conn.commit()
    cur.close()
    conn.close()

    flash("Notícia publicada com sucesso!", "success")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/noticia/editar/<int:id>", methods=["GET", "POST"])
@admin_necessario
def admin_editar_noticia(id):
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        subtitulo = request.form.get("subtitulo", "").strip()
        categoria = request.form.get("categoria", "Geral").strip()
        imagem_url = request.form.get("imagem_url", "").strip()
        conteudo = request.form.get("conteudo", "").strip()
        destaque = True if request.form.get("destaque") else False
        no_banner = True if request.form.get("no_banner") else False

        cur.execute("""
            UPDATE noticias 
            SET titulo = %s, subtitulo = %s, categoria = %s, imagem_url = %s, conteudo = %s, destaque = %s, no_banner = %s
            WHERE id = %s;
        """, (titulo, subtitulo, categoria, imagem_url, conteudo, destaque, no_banner, id))

        conn.commit()
        cur.close()
        conn.close()

        flash("Notícia atualizada com sucesso!", "success")
        return redirect(url_for("admin_dashboard"))

    cur.execute("SELECT * FROM noticias WHERE id = %s;", (id,))
    noticia = cur.fetchone()
    cur.close()
    conn.close()

    if not noticia:
        flash("Notícia não encontrada.", "error")
        return redirect(url_for("admin_dashboard"))

    return render_template("admin_editar_noticia.html", noticia=noticia)


@app.route("/admin/noticia/excluir/<int:id>", methods=["POST"])
@admin_necessario
def admin_excluir_noticia(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM noticias WHERE id = %s;", (id,))
    conn.commit()

    cur.close()
    conn.close()

    flash("Notícia removida.", "info")
    return redirect(url_for("admin_dashboard"))


# ------------------------------------------------------------------------------
# ADMIN: PRODUTOS DA LOJA (CRIAR COM UPLOAD, EDITAR E EXCLUIR)
# ------------------------------------------------------------------------------
@app.route("/admin/produto/criar", methods=["POST"])
@admin_necessario
def admin_criar_produto():
    nome = request.form.get("nome", "").strip()
    categoria = request.form.get("categoria", "Acessórios").strip()
    equipe_id = request.form.get("equipe_id") or None
    preco = float(request.form.get("preco", 0.0))
    descricao = request.form.get("descricao", "").strip()
    estoque = int(request.form.get("estoque", 10))
    tag = request.form.get("tag", "Disponível").strip()
    destaque = True if request.form.get("destaque") else False
    no_banner_home = True if request.form.get("no_banner_home") else False
    no_banner_loja = True if request.form.get("no_banner_loja") else False

    imagem_url = request.form.get("imagem_url", "").strip()
    arquivo_foto = request.files.get("foto_arquivo")

    if arquivo_foto and arquivo_foto.filename:
        nome_seguro = secure_filename(arquivo_foto.filename)
        caminho_salvar = os.path.join(UPLOAD_PRODUTOS, nome_seguro)
        arquivo_foto.save(caminho_salvar)
        imagem_url = f"/static/images/produtos/{nome_seguro}"
    elif not imagem_url:
        imagem_url = "https://images.unsplash.com/photo-1588850561407-ed78c282e89b?auto=format&fit=crop&w=800&q=80"

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO produtos (nome, categoria, equipe_id, preco, descricao, imagem_url, estoque, tag, destaque, no_banner_home, no_banner_loja)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
    """, (nome, categoria, equipe_id, preco, descricao, imagem_url, estoque, tag, destaque, no_banner_home, no_banner_loja))
    novo_prod_id = cur.fetchone()["id"]

    # Cria banner na Home se marcado
    if no_banner_home:
        cur.execute("""
            INSERT INTO banners (titulo, subtitulo, imagem_url, link_url, tag_destaque, local_exibicao, produto_id)
            VALUES (%s, %s, %s, %s, %s, 'home', %s);
        """, (f"{nome} • R$ {preco:.2f}", descricao or "Disponível na Fan Store Oficial", imagem_url, "/loja", f"LOJA: {tag.upper()}", novo_prod_id))

    # Cria banner exclusivo da Loja se marcado
    if no_banner_loja:
        cur.execute("""
            INSERT INTO banners (titulo, subtitulo, imagem_url, link_url, tag_destaque, local_exibicao, produto_id)
            VALUES (%s, %s, %s, %s, %s, 'loja', %s);
        """, (f"{nome} • R$ {preco:.2f}", descricao or "Garanta já o seu na Loja Oficial", imagem_url, "/loja", tag.upper(), novo_prod_id))

    conn.commit()
    cur.close()
    conn.close()

    flash("Produto cadastrado com sucesso na Loja Oficial!", "success")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/produto/editar/<int:id>", methods=["GET", "POST"])
@admin_necessario
def admin_editar_produto(id):
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        categoria = request.form.get("categoria", "Acessórios").strip()
        equipe_id = request.form.get("equipe_id") or None
        preco = float(request.form.get("preco", 0.0))
        descricao = request.form.get("descricao", "").strip()
        estoque = int(request.form.get("estoque", 10))
        tag = request.form.get("tag", "Disponível").strip()
        destaque = True if request.form.get("destaque") else False
        no_banner_home = True if request.form.get("no_banner_home") else False
        no_banner_loja = True if request.form.get("no_banner_loja") else False

        imagem_url = request.form.get("imagem_url", "").strip()
        arquivo_foto = request.files.get("foto_arquivo")

        if arquivo_foto and arquivo_foto.filename:
            nome_seguro = secure_filename(arquivo_foto.filename)
            caminho_salvar = os.path.join(UPLOAD_PRODUTOS, nome_seguro)
            arquivo_foto.save(caminho_salvar)
            imagem_url = f"/static/images/produtos/{nome_seguro}"

        cur.execute("""
            UPDATE produtos 
            SET nome = %s, categoria = %s, equipe_id = %s, preco = %s, descricao = %s,
                imagem_url = COALESCE(NULLIF(%s, ''), imagem_url),
                estoque = %s, tag = %s, destaque = %s, no_banner_home = %s, no_banner_loja = %s
            WHERE id = %s;
        """, (nome, categoria, equipe_id, preco, descricao, imagem_url, estoque, tag, destaque, no_banner_home, no_banner_loja, id))

        conn.commit()
        cur.close()
        conn.close()

        flash("Produto atualizado na Loja Oficial!", "success")
        return redirect(url_for("admin_dashboard"))

    cur.execute("SELECT * FROM produtos WHERE id = %s;", (id,))
    produto = cur.fetchone()

    cur.execute("SELECT id, nome FROM equipes ORDER BY nome ASC;")
    equipes = cur.fetchall()

    cur.close()
    conn.close()

    if not produto:
        flash("Produto não encontrado.", "error")
        return redirect(url_for("admin_dashboard"))

    return render_template("admin_editar_produto.html", produto=produto, equipes=equipes)


@app.route("/admin/produto/excluir/<int:id>", methods=["POST"])
@admin_necessario
def admin_excluir_produto(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM produtos WHERE id = %s;", (id,))
    conn.commit()

    cur.close()
    conn.close()

    flash("Produto excluído da loja com sucesso.", "info")
    return redirect(url_for("admin_dashboard"))


# ------------------------------------------------------------------------------
# ADMIN: BANNERS (CRIAR E EXCLUIR)
# ------------------------------------------------------------------------------
@app.route("/admin/banner/criar", methods=["POST"])
@admin_necessario
def admin_criar_banner():
    titulo = request.form.get("titulo", "").strip()
    subtitulo = request.form.get("subtitulo", "").strip()
    imagem_url = request.form.get("imagem_url", "").strip()
    link_url = request.form.get("link_url", "/").strip()
    tag_destaque = request.form.get("tag_destaque", "DESTAQUE").strip()
    local_exibicao = request.form.get("local_exibicao", "home").strip()
    ordem = int(request.form.get("ordem", 1))

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO banners (titulo, subtitulo, imagem_url, link_url, tag_destaque, local_exibicao, ordem)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """, (titulo, subtitulo, imagem_url, link_url, tag_destaque, local_exibicao, ordem))

    conn.commit()
    cur.close()
    conn.close()

    flash("Slide adicionado ao carrossel com sucesso!", "success")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/banner/excluir/<int:id>", methods=["POST"])
@admin_necessario
def admin_excluir_banner(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM banners WHERE id = %s;", (id,))
    conn.commit()

    cur.close()
    conn.close()

    flash("Banner removido.", "info")
    return redirect(url_for("admin_dashboard"))


# ------------------------------------------------------------------------------
# ADMIN: GALERIA DE FOTOS (CRIAR E EXCLUIR)
# ------------------------------------------------------------------------------
@app.route("/admin/galeria/criar", methods=["POST"])
@admin_necessario
def admin_criar_foto_galeria():
    titulo = request.form.get("titulo", "").strip()
    categoria = request.form.get("categoria", "Paddock").strip()
    descricao = request.form.get("descricao", "").strip()

    imagem_url = request.form.get("imagem_url", "").strip()
    arquivo_foto = request.files.get("foto_arquivo")

    if arquivo_foto and arquivo_foto.filename:
        nome_seguro = secure_filename(arquivo_foto.filename)
        caminho_salvar = os.path.join(UPLOAD_GALERIA, nome_seguro)
        arquivo_foto.save(caminho_salvar)
        imagem_url = f"/static/images/galeria/{nome_seguro}"
    elif not imagem_url:
        imagem_url = "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=1200&q=80"

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO galeria (titulo, categoria, imagem_url, descricao)
        VALUES (%s, %s, %s, %s);
    """, (titulo, categoria, imagem_url, descricao))

    conn.commit()
    cur.close()
    conn.close()

    flash("Foto adicionada à galeria com sucesso!", "success")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/galeria/excluir/<int:id>", methods=["POST"])
@admin_necessario
def admin_excluir_foto_galeria(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM galeria WHERE id = %s;", (id,))
    conn.commit()

    cur.close()
    conn.close()

    flash("Foto removida da galeria.", "info")
    return redirect(url_for("admin_dashboard"))


# ==============================================================================
# ROTA 9: SOBRE NÓS & CONTATOS COM FEEDBACK
# ==============================================================================
@app.route("/sobre", methods=["GET", "POST"])
def sobre():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        tipo_feedback = request.form.get("tipo_feedback", "").strip()
        assunto = request.form.get("assunto", "").strip()
        mensagem = request.form.get("mensagem", "").strip()

        if not (nome and email and tipo_feedback and assunto and mensagem):
            flash("Por favor, preencha todos os campos do formulário.", "error")
            return redirect(url_for("sobre"))

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO contatos (nome, email, tipo_feedback, assunto, mensagem)
            VALUES (%s, %s, %s, %s, %s);
        """, (nome, email, tipo_feedback, assunto, mensagem))

        conn.commit()
        cur.close()
        conn.close()

        flash("Obrigado pelo seu feedback sobre o Setor F1! Sua mensagem foi enviada.", "success")
        return redirect(url_for("sobre"))

    return render_template("sobre.html")


# ==============================================================================
# ROTA 10: FEEDBACKS PÚBLICOS
# ==============================================================================
@app.route("/mensagens")
def mensagens():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contatos ORDER BY data_envio DESC;")
    mensagens = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("mensagens.html", mensagens=mensagens)


# ==============================================================================
# INICIALIZAÇÃO DO SERVIDOR LOCAL
# ==============================================================================
if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "True").lower() == "true"
    print("\n Servidor Setor F1 iniciando em: http://127.0.0.1:5000\n")
    app.run(host="127.0.0.1", port=5000, debug=debug_mode)
