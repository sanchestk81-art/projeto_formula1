import sqlite3

def conectar():
    """Cria a conexão com o banco e garante a criação da tabela correta ('resultados')."""
    conn = sqlite3.connect('formula1.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resultados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ano INTEGER,
            circuito TEXT,
            piloto TEXT,
            equipe TEXT,
            numero INTEGER,
            posicao INTEGER,
            pontos INTEGER,
            pole_position TEXT
        )
    ''')
    conn.commit()
    return conn

def criar_tabela():
    """Função de compatibilidade (apenas chama o conectar para garantir a tabela)."""
    conn = conectar()
    conn.close()

def salvar_no_banco(lista_resultados):
    """Insere a lista de dicionários vinda do sistema na tabela resultados."""
    conn = conectar()
    cursor = conn.cursor()
    for item in lista_resultados:
        cursor.execute('''
            INSERT INTO resultados (ano, circuito, piloto, equipe, numero, posicao, pontos, pole_position)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            item['ano'],
            item['circuito'].strip(), # Limpa espaços extras
            item['piloto'],
            item['equipe'],
            item['numero'],
            item['posicao'],
            item['pontos'],
            item['pole_position']
        ))
    conn.commit()
    conn.close()

def contar_corridas(ano):
    """Retorna a quantidade de circuitos distintos já cadastrados no ano especificado."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(DISTINCT circuito) FROM resultados WHERE ano = ?', (ano,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado and resultado[0] else 0

def circuito_ja_cadastrado(ano, circuito):
    """Verifica se um circuito já foi cadastrado em determinado ano (ignorando maiúsculas/minúsculas)."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT COUNT(*) FROM resultados WHERE ano = ? AND LOWER(circuito) = LOWER(?)',
        (ano, circuito.strip())
    )
    existe = cursor.fetchone()[0] > 0
    conn.close()
    return existe

def buscar_campeao_mundial(ano):
    """Soma a pontuação por piloto e retorna o 1º colocado (Piloto, Equipe, Total de Pontos)."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT piloto, equipe, SUM(pontos) as total_pontos 
        FROM resultados 
        WHERE ano = ? 
        GROUP BY piloto, equipe
        ORDER BY total_pontos DESC 
        LIMIT 1
    ''', (ano,))
    campeao = cursor.fetchone()
    conn.close()
    return campeao

def buscar_equipe_campea(ano):
    """Soma a pontuação por equipe e retorna a 1ª colocada (Equipe, Total de Pontos)."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT equipe, SUM(pontos) as total_pontos 
        FROM resultados 
        WHERE ano = ? 
        GROUP BY equipe 
        ORDER BY total_pontos DESC 
        LIMIT 1
    ''', (ano,))
    equipe_campea = cursor.fetchone()
    conn.close()
    return equipe_campea

def buscar_resultado_corrida(ano, circuito):
    """Busca o resultado de uma corrida específica tratando maiúsculas/minúsculas e espaços."""
    conexao = conectar()
    cursor = conexao.cursor()

    circuito_formatado = f"%{circuito.strip()}%"

    cursor.execute("""
        SELECT posicao, piloto, equipe, numero, pontos, pole_position
        FROM resultados
        WHERE ano = ? AND LOWER(circuito) LIKE LOWER(?)
        ORDER BY posicao ASC
    """, (ano, circuito_formatado))

    resultados = cursor.fetchall()
    conexao.close()
    return resultados


import importlib


def inicializar_dados_historicos():
    """
    Varre os arquivos de 2020 a 2026 (nomeados como 2020.py, 2021.py...)
    na pasta 'dados_temporada' e insere no banco de dados.
    """
    print("🔄 Verificando e importando dados históricos (2020 a 2026)...")

    for ano in range(2020, 2027):
        try:
            # Usa o importlib para conseguir importar arquivos com nomes numéricos (ex: 2020.py)
            modulo_nome = f"dados_temporada.{ano}"
            temporada_modulo = importlib.import_module(modulo_nome)

            # Tenta pegar a variável de dados de dentro do arquivo.
            # (Caso dentro de 2023.py a lista se chame 'corridas_2023', 'corridas' ou 'dados',
            # tentamos as opções mais comuns para evitar erro)
            if hasattr(temporada_modulo, f"corridas_{ano}"):
                dados = getattr(temporada_modulo, f"corridas_{ano}")
            elif hasattr(temporada_modulo, "corridas"):
                dados = temporada_modulo.corridas
            elif hasattr(temporada_modulo, "dados"):
                dados = temporada_modulo.dados
            else:
                print(f"⚠️ O arquivo {ano}.py não possui uma variável de dados reconhecida.")
                continue

        except ModuleNotFoundError:
            # Se o arquivo do ano não existir, apenas pula para o próximo
            continue
        except Exception as e:
            print(f"⚠️ Erro ao carregar o arquivo {ano}.py: {e}")
            continue

        # Verifica se já existem corridas cadastradas para este ano no banco
        corridas_existentes = contar_corridas(ano)
        if corridas_existentes > 0:
            continue

        print(f"📥 Carregando temporada {ano} para o banco pela primeira vez...")

        circuitos_unicos = set(c['circuito'] for c in dados)

        for circuito in circuitos_unicos:
            resultados_circuito = [c for c in dados if c['circuito'].lower() == circuito.lower()]
            salvar_no_banco(resultados_circuito)

        print(f"   -> Temporada {ano} salva com sucesso no banco!")

    print("✅ Banco de dados atualizado com os históricos disponíveis.")