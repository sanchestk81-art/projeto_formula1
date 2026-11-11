"""
script.py
---------
Script responsável por criar o banco de dados 'formula1' (caso ainda não exista)
e todas as tabelas completas para o Setor F1:
- equipes: Dados completos, carros, motores e pilotos titulares/reservas vinculados.
- pilotos: Informações, fotos, equipe, papel (titular/reserva), pontos na temporada e chances de título.
- noticias: Notícias gerenciadas e editáveis pelo admin.
- corridas: Corridas históricas com Pódio, Pole Position, Volta Rápida e Classificação da prova.
- produtos: Loja oficial com fotos, tags (Mais Vendido, Edição Limitada, etc.) e banner da loja.
- pedidos: Compras efetuadas pelos clientes cadastrados.
- banners: Banners rotativos editáveis da página principal e da loja oficial.
- galeria: Acervo de fotos de alta definição do paddock, carros e pódios.
- contatos: Feedbacks e sugestões dos usuários.
- usuarios: Administradores e clientes/fãs.
"""

import os
import psycopg2
from dotenv import load_dotenv

# Carrega as configurações do .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "formula1")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "1234")


def criar_banco_se_nao_existir():
    """Conecta ao banco padrão 'postgres' e cria o banco 'formula1' se não existir."""
    print(" Verificando existência do banco de dados...")
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname="postgres",
            user=DB_USER,
            password=DB_PASSWORD
        )
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
        existe = cur.fetchone()

        if not existe:
            cur.execute(f'CREATE DATABASE "{DB_NAME}"')
            print(f" Banco de dados '{DB_NAME}' criado com sucesso!")
        else:
            print(f" Banco de dados '{DB_NAME}' já existe.")

        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print(f"  Aviso ao verificar banco 'postgres': {e}")


DDL_TABELAS = """
-- Remove tabelas se existirem para aplicar a nova estrutura limpa
DROP TABLE IF EXISTS galeria, banners, pedidos, produtos, contatos, corridas, pilotos, noticias, equipes, usuarios CASCADE;

-- 1. Tabela de Equipes (com modelo e imagem do carro)
CREATE TABLE IF NOT EXISTS equipes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE,
    nome_completo VARCHAR(150) NOT NULL,
    pais_origem VARCHAR(80) NOT NULL,
    sede VARCHAR(120),
    chefe_equipe VARCHAR(100),
    motor VARCHAR(80),
    titulos_construtores INT DEFAULT 0,
    ano_estreia INT,
    historia TEXT NOT NULL,
    logo_url TEXT,
    carro_modelo VARCHAR(100),
    carro_imagem_url TEXT,
    cor_primaria VARCHAR(10) DEFAULT '#E10600'
);

-- 2. Tabela de Pilotos (com papel titular/reserva, pontuação e chances de título)
CREATE TABLE IF NOT EXISTS pilotos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    numero INT,
    nacionalidade VARCHAR(80) NOT NULL,
    pais_codigo VARCHAR(5) DEFAULT 'br',
    equipe_id INT REFERENCES equipes(id) ON DELETE SET NULL,
    foto_url TEXT,
    como_entrou_f1 TEXT NOT NULL,
    trajetoria_f1 TEXT NOT NULL,
    titulos_mundiais INT DEFAULT 0,
    vitorias INT DEFAULT 0,
    podios INT DEFAULT 0,
    data_nascimento DATE,
    ativo BOOLEAN DEFAULT TRUE,
    papel_equipe VARCHAR(30) DEFAULT 'titular', -- 'titular' ou 'reserva'
    temporadas_ativas VARCHAR(100),
    pontos_temporada INT DEFAULT 0,
    chance_titulo NUMERIC(5, 2) DEFAULT 0.0
);

-- 3. Tabela de Usuários (Admins e Clientes/Fãs)
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL,
    tipo VARCHAR(20) NOT NULL DEFAULT 'cliente', -- 'admin' ou 'cliente'
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Tabela de Notícias (Editáveis pelo Admin)
CREATE TABLE IF NOT EXISTS noticias (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    subtitulo VARCHAR(350),
    conteudo TEXT NOT NULL,
    data_publicacao DATE NOT NULL DEFAULT CURRENT_DATE,
    categoria VARCHAR(50) DEFAULT 'Notícias',
    imagem_url TEXT,
    autor VARCHAR(100) DEFAULT 'Redação Setor F1',
    destaque BOOLEAN DEFAULT FALSE,
    no_banner BOOLEAN DEFAULT FALSE,
    criado_por_id INT REFERENCES usuarios(id) ON DELETE SET NULL
);

-- 5. Tabela de Corridas (com Pole Position, Pódio 1º/2º/3º, Volta Rápida e Classificação)
CREATE TABLE IF NOT EXISTS corridas (
    id SERIAL PRIMARY KEY,
    ano INT NOT NULL DEFAULT 2026,
    rodada INT NOT NULL,
    nome_gp VARCHAR(150) NOT NULL,
    circuito VARCHAR(150) NOT NULL,
    pais VARCHAR(80) NOT NULL,
    pais_codigo VARCHAR(10) DEFAULT 'br',
    cidade VARCHAR(80),
    data_corrida DATE NOT NULL,
    status VARCHAR(20) NOT NULL, -- 'concluida' ou 'proxima'
    pole_position_piloto_id INT REFERENCES pilotos(id) ON DELETE SET NULL,
    pole_position_tempo VARCHAR(50),
    vencedor_piloto_id INT REFERENCES pilotos(id) ON DELETE SET NULL, -- 1º lugar
    vencedor_equipe VARCHAR(100),
    segundo_piloto_id INT REFERENCES pilotos(id) ON DELETE SET NULL, -- 2º lugar
    segundo_lugar VARCHAR(100),
    terceiro_piloto_id INT REFERENCES pilotos(id) ON DELETE SET NULL, -- 3º lugar
    terceiro_lugar VARCHAR(100),
    volta_rapida_piloto_id INT REFERENCES pilotos(id) ON DELETE SET NULL,
    volta_mais_rapida VARCHAR(100),
    noticias_resumo TEXT,
    classificacao_detalhada TEXT, -- JSON ou lista textual da classificação completa
    imagem_circuito_url TEXT
);

-- 6. Tabela de Contatos e Feedbacks
CREATE TABLE IF NOT EXISTS contatos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL,
    tipo_feedback VARCHAR(30) NOT NULL,
    assunto VARCHAR(150) NOT NULL,
    mensagem TEXT NOT NULL,
    data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 7. Tabela de Produtos (Loja Oficial com tags, fotos e banner da loja)
CREATE TABLE IF NOT EXISTS produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    equipe_id INT REFERENCES equipes(id) ON DELETE SET NULL,
    preco NUMERIC(10, 2) NOT NULL,
    descricao TEXT,
    imagem_url TEXT NOT NULL,
    estoque INT DEFAULT 50,
    tag VARCHAR(50) DEFAULT 'Disponível', -- 'Mais Vendido', 'Edição Limitada', 'Nova Coleção', 'Exclusivo'
    destaque BOOLEAN DEFAULT FALSE,
    no_banner_home BOOLEAN DEFAULT FALSE,
    no_banner_loja BOOLEAN DEFAULT FALSE
);

-- 8. Tabela de Pedidos da Loja
CREATE TABLE IF NOT EXISTS pedidos (
    id SERIAL PRIMARY KEY,
    usuario_id INT REFERENCES usuarios(id) ON DELETE CASCADE,
    produto_id INT REFERENCES produtos(id) ON DELETE CASCADE,
    quantidade INT NOT NULL DEFAULT 1,
    valor_total NUMERIC(10, 2) NOT NULL,
    status VARCHAR(30) DEFAULT 'Confirmado',
    endereco_entrega VARCHAR(255),
    data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 9. Tabela de Banners Rotativos (Para a Home e para a Loja)
CREATE TABLE IF NOT EXISTS banners (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    subtitulo VARCHAR(350),
    imagem_url TEXT NOT NULL,
    link_url VARCHAR(255) DEFAULT '/',
    tag_destaque VARCHAR(50) DEFAULT 'DESTAQUE SETOR F1',
    local_exibicao VARCHAR(30) DEFAULT 'home', -- 'home' ou 'loja'
    produto_id INT REFERENCES produtos(id) ON DELETE SET NULL,
    ordem INT DEFAULT 1,
    ativo BOOLEAN DEFAULT TRUE,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 10. Tabela de Galeria de Fotos do Paddock & Corridas
CREATE TABLE IF NOT EXISTS galeria (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    categoria VARCHAR(50) DEFAULT 'Paddock', -- 'Carros', 'Pódio', 'Paddock', 'Bastidores', 'Chuva'
    imagem_url TEXT NOT NULL,
    descricao TEXT,
    data_registro DATE DEFAULT CURRENT_DATE
);
"""


def criar_tabelas():
    """Conecta no banco 'formula1' e cria todas as tabelas usando cursor nativo."""
    criar_banco_se_nao_existir()

    print("\n Conectando ao banco de dados para criar tabelas completas do Setor F1...")
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cur = conn.cursor()

        cur.execute(DDL_TABELAS)
        conn.commit()

        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            ORDER BY table_name;
        """)
        tabelas = cur.fetchall()

        print("\n Tabelas geradas com sucesso no PostgreSQL:")
        for t in tabelas:
            print(f"   [OK] {t[0]}")

        cur.close()
        conn.close()
        print("\n Estrutura do banco de dados configurada com êxito!")

    except psycopg2.Error as erro:
        print(f"\n[ERRO] Falha ao criar tabelas: {erro}")
        raise erro


if __name__ == "__main__":
    criar_tabelas()
