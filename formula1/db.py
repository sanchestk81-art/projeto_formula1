import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "formula1")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "1234")


def get_db_connection(use_dict_cursor=True):
    """
    Cria e retorna uma conexão direta com o banco de dados PostgreSQL.
    Não utiliza ORM. O cursor padrão é RealDictCursor, permitindo
    acessar as colunas como dicionário (ex: linha['nome']).
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            cursor_factory=RealDictCursor if use_dict_cursor else None
        )
        return conn
    except psycopg2.Error as erro:
        print(f"[ERRO DE CONEXÃO COM O BANCO]: {erro}")
        raise erro
