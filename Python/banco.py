import sqlite3

def conectar():
    """Cria a conexão com o banco e garante a criação da tabela com as colunas corretas."""
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


def salvar_no_banco(lista_resultados):
    """Insere a lista de dicionários vinda do main.py na tabela resultados."""
    conn = conectar()
    cursor = conn.cursor()
    for item in lista_resultados:
        cursor.execute('''
            INSERT INTO resultados (ano, circuito, piloto, equipe, numero, posicao, pontos, pole_position)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            item['ano'],
            item['circuito'],
            item['piloto'],
            item['equipe'],
            item['numero'],
            item['posicao'],
            item['pontos'],
            item['pole_position']
        ))
    conn.commit()
    conn.close()
    print("\n✅ Corrida registrada com sucesso no SQLite!")


def contar_corridas(ano):
    """Retorna a quantidade de circuitos distintos já cadastrados no ano especificado."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(DISTINCT circuito) FROM resultados WHERE ano = ?', (ano,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado and resultado[0] else 0


def circuito_ja_cadastrado(ano, circuito):
    """Verifica se um circuito já foi cadastrado em determinado ano."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT COUNT(*) FROM resultados WHERE ano = ? AND circuito = ?',
        (ano, circuito)
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