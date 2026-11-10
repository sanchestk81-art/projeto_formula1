import sqlite3

# Conecta ao banco de dados
conexao = sqlite3.connect("../formula1.db")
cursor = conexao.cursor()

# 1. Verifica se a tabela 'resultados' existe e quantas linhas ela tem
cursor.execute("SELECT COUNT(*) FROM resultados")
total = cursor.fetchone()[0]
print(f"Total de registros na tabela 'resultados': {total}")

# 2. Mostra alguns circuitos que estão salvos no banco para o ano 2023
cursor.execute(
    "SELECT DISTINCT ano, circuito FROM resultados WHERE ano = 2023"
)
registros = cursor.fetchall()
print("\nCircuitos salvos no banco para o ano 2023:")
for reg in registros:
    print(reg)

conexao.close()