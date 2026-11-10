import os

print("Pasta atual:", os.getcwd())
print("Conteúdo da pasta atual:", os.listdir())

# Tenta ver se a pasta dados_temporada existe
if os.path.exists("../dados_temporada"):
  print("✅ A pasta 'dados_temporada' foi encontrada!")
  print("Conteúdo da pasta dados_temporada:", os.listdir("../dados_temporada"))
else:
  print(
      "❌ ERRO: A pasta 'dados_temporada' NÃO foi encontrada no mesmo diretório"
      " do script!"
  )

# Tenta importar o ano de 2023 manualmente para ver o erro exato
try:
  from dados_temporada import temporada_2023

  print(
      "✅ Módulo temporada_2023 importado com sucesso! Total de corridas:"
      f" {len(temporada_2023.corridas_2023)}"
  )
except Exception as e:
  print(f"❌ Erro ao tentar importar temporada_2023: {e}")