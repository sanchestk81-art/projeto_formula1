import banco
from Python.informações_pilotos import PILOTOS_POR_ANO
from Python.informações_pilotos import PONTOS_F1

# --- INICIALIZAÇÃO OBRIGATÓRIA DO BANCO E HISTÓRICOS ---
banco.criar_tabela()
banco.inicializar_dados_historicos()


def cadastrar_corrida():
  print("=" * 50)
  print("      SISTEMA DE GERENCIAMENTO DE CORRIDAS F1      ")
  print("=" * 50)

  ano = int(input("Digite o ano da temporada (ex: 2026): "))

  # Verifica quantas corridas já aconteceram no ano
  corridas_feitas = banco.contar_corridas(ano)

  if corridas_feitas >= 24:
    print(
        f"\n⚠️ O campeonato de {ano} já atingiu o limite de 24 corridas e foi"
        " ENCERRADO!"
    )
    consultar_campeonato()
    return

  numero_corrida_atual = corridas_feitas + 1
  print(
      f"\n📌 Registrando a Corrida {numero_corrida_atual} de 24 do ano {ano}"
  )

  circuito = input("Nome do circuito (ex: Interlagos): ")
  pole_position = input("Quem fez a Pole Position? ").strip()

  print("\n--- DIGITE A ORDEM DE CHEGADA (1º ao 22º Lugar) ---")
  resultados_corrida = []

  for posicao in range(1, 23):
    nome_piloto = input(f"Digite o piloto do {posicao}º lugar: ").strip()

    # BUSCA NO DICIONÁRIO DE PILOTOS: Pega equipe e número automaticamente
    dados_cadastro = PILOTOS_POR_ANO.get(
        nome_piloto, {"numero": 0, "equipe": "Indefinida"}
    )

    pontos = PONTOS_F1.get(posicao, 0)
    fez_pole = "Sim" if nome_piloto.lower() == pole_position.lower() else "Não"

    # DICIONÁRIO com os dados completos do resultado
    registro = {
        "ano": ano,
        "circuito": circuito,
        "piloto": nome_piloto,
        "equipe": dados_cadastro["equipe"],
        "numero": dados_cadastro["numero"],
        "posicao": posicao,
        "pontos": pontos,
        "pole_position": fez_pole,
    }

    resultados_corrida.append(registro)

  # Grava no banco de dados
  banco.salvar_no_banco(resultados_corrida)
  print(
      f"\n✅ Corrida {numero_corrida_atual} em {circuito} cadastrada com"
      " sucesso!"
  )

  # Verifica se essa foi a última corrida para encerrar o campeonato
  if numero_corrida_atual == 24:
    print("\n🏁 A 24ª CORRIDA FOI CONCLUÍDA! FIM DA TEMPORADA! 🏁")
    consultar_campeonato()

def consultar_campeonato():
    print("=" * 50)
    print("          CLASSIFICAÇÃO E CAMPEÕES DO MUNDO         ")
    print("=" * 50)

    try:
        ano = int(input("Digite o ano da temporada que deseja consultar (ex: 2023): "))
    except ValueError:
        print("❌ Ano inválido. Digite apenas números.")
        return

    # Busca o campeão de pilotos
    campeao_piloto = banco.buscar_campeao_mundial(ano)
    # Busca a equipe campeã
    equipe_campea = banco.buscar_equipe_campea(ano)

    if not campeao_piloto and not equipe_campea:
        print(f"\n⚠️ Nenhum dado encontrado para o ano {ano}.")
        return

    print(f"\n🏆 CAMPEONATO MUNDIAL DE F1 ({ano}) 🏆")
    print("-" * 50)

    if campeao_piloto:
        piloto_nome, equipe_piloto, pontos_piloto = campeao_piloto
        print(f"🥇 Campeão de Pilotos: {piloto_nome} ({equipe_piloto}) - {pontos_piloto} pontos")
    else:
        print("🥇 Campeão de Pilotos: Dados não disponíveis.")

    if equipe_campea:
        nome_equipe, pontos_equipe = equipe_campea
        print(f"🏆 Construtores Campeões: {nome_equipe} - {pontos_equipe} pontos")
    else:
        print("🏆 Construtores Campeões: Dados não disponíveis.")

    print("-" * 50)

def consultar_resultado_corrida():
    print("=" * 50)
    print("         CONSULTAR RESULTADO DE UMA CORRIDA         ")
    print("=" * 50)

    try:
        ano = int(input("Digite o ano da temporada (ex: 2023): "))
    except ValueError:
        print("❌ Ano inválido. Digite apenas números.")
        return

    circuito = input("Digite o nome do circuito (ex: Monaco, Interlagos, Sakhir): ")

    # Busca os resultados no banco
    resultados = banco.buscar_resultado_corrida(ano, circuito)

    if not resultados:
        print(f"\n⚠️ Nenhum resultado encontrado para o circuito '{circuito}' no ano {ano}.")
        return

    print(f"\n🏁 RESULTADOS DA CORRIDA EM {circuito.upper()} ({ano}) 🏁")
    print("-" * 78)
    print(f"{'Pos':<5} | {'Piloto':<25} | {'Equipe':<20} | {'Pts':<5} | {'Pole?'}")
    print("-" * 78)

    for linha in resultados:
        posicao, piloto, equipe, numero, pontos, pole_position = linha
        print(f"{str(posicao) + 'º':<5} | {piloto:<25} | {equipe:<20} | {str(pontos):<5} | {pole_position}")

    print("-" * 78)


def menu():
    while True:
        print("\n==================================")
        print("          MENU FORMULA 1          ")
        print("==================================")
        print("1. Cadastrar Nova Corrida")
        print("2. Ver Classificação do Campeonato")
        print("3. Ver Resultado de uma Corrida Específica")
        print("4. Sair")

        escolha = input("Escolha uma opção (1-4): ").strip()

        if escolha == '1':
            cadastrar_corrida()  # <--- CHAMANDO A FUNÇÃO DE CADASTRO AQUI!
        elif escolha == '2':
            consultar_campeonato()
        elif escolha == '3':
            consultar_resultado_corrida()
        elif escolha == '4':
            print("\nSaindo do sistema. Até mais!")
            break
        else:
            print("\n❌ Opção inválida! Escolha um número de 1 a 4.")


if __name__ == "__main__":
    menu()