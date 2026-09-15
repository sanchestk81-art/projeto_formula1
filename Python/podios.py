import banco

# DICIONÁRIO: Chaves sem espaços extras e com padrão unificado
PILOTOS_TEMPORADA = {
    # Aceita nome completo ou apenas sobrenome para evitar erros do usuário
    "max verstappen": {"nome_oficial": "Verstappen", "numero": 1, "equipe": "Red Bull Racing"},
    "verstappen": {"nome_oficial": "Verstappen", "numero": 1, "equipe": "Red Bull Racing"},

    "yuki tsunoda": {"nome_oficial": "Tsunoda", "numero": 22, "equipe": "Red Bull Racing"},
    "tsunoda": {"nome_oficial": "Tsunoda", "numero": 22, "equipe": "Red Bull Racing"},

    "lewis hamilton": {"nome_oficial": "Hamilton", "numero": 44, "equipe": "Ferrari"},
    "hamilton": {"nome_oficial": "Hamilton", "numero": 44, "equipe": "Ferrari"},

    "charles leclerc": {"nome_oficial": "Leclerc", "numero": 16, "equipe": "Ferrari"},
    "leclerc": {"nome_oficial": "Leclerc", "numero": 16, "equipe": "Ferrari"},

    "lando norris": {"nome_oficial": "Norris", "numero": 4, "equipe": "McLaren"},
    "norris": {"nome_oficial": "Norris", "numero": 4, "equipe": "McLaren"},

    "oscar piastri": {"nome_oficial": "Piastri", "numero": 81, "equipe": "McLaren"},
    "piastri": {"nome_oficial": "Piastri", "numero": 81, "equipe": "McLaren"},

    "george russel": {"nome_oficial": "Russell", "numero": 63, "equipe": "Mercedes"},
    "russel": {"nome_oficial": "Russell", "numero": 63, "equipe": "Mercedes"},

    "andrea antonelli": {"nome_oficial": "Antonelli", "numero": 12, "equipe": "Mercedes"},
    "antonelli": {"nome_oficial": "Antonelli", "numero": 12, "equipe": "Mercedes"},

    "fernando alonso": {"nome_oficial": "Alonso", "numero": 14, "equipe": "Aston Martin"},
    "alonso": {"nome_oficial": "Alonso", "numero": 14, "equipe": "Aston Martin"},

    "lance stroll": {"nome_oficial": "Stroll", "numero": 18, "equipe": "Aston Martin"},
    "stroll": {"nome_oficial": "Stroll", "numero": 18, "equipe": "Aston Martin"},

    "pierre gasly": {"nome_oficial": "Gasly", "numero": 10, "equipe": "Alpine"},
    "gasly": {"nome_oficial": "Gasly", "numero": 10, "equipe": "Alpine"},

    "franco colapinto": {"nome_oficial": "Colapinto", "numero": 43, "equipe": "Alpine"},
    "colapinto": {"nome_oficial": "Colapinto", "numero": 43, "equipe": "Alpine"},

    "alex albon": {"nome_oficial": "Albon", "numero": 23, "equipe": "Williams"},
    "albon": {"nome_oficial": "Albon", "numero": 23, "equipe": "Williams"},

    "carlos sainz": {"nome_oficial": "Sainz", "numero": 55, "equipe": "Williams"},
    "sainz": {"nome_oficial": "Sainz", "numero": 55, "equipe": "Williams"},

    "arvid lindblad": {"nome_oficial": "Lindblad", "numero": 41, "equipe": "RB"},
    "lindblad": {"nome_oficial": "Lindblad", "numero": 41, "equipe": "RB"},

    "liam lawson": {"nome_oficial": "Lawson", "numero": 30, "equipe": "RB"},
    "lawson": {"nome_oficial": "Lawson", "numero": 30, "equipe": "RB"},

    "nico hulkenberg": {"nome_oficial": "Hulkenberg", "numero": 27, "equipe": "Audi"},
    "hulkenberg": {"nome_oficial": "Hulkenberg", "numero": 27, "equipe": "Audi"},

    "gabriel bortoleto": {"nome_oficial": "Bortoleto", "numero": 5, "equipe": "Audi"},
    "bortoleto": {"nome_oficial": "Bortoleto", "numero": 5, "equipe": "Audi"},

    "esteban ocon": {"nome_oficial": "Ocon", "numero": 31, "equipe": "Haas"},
    "ocon": {"nome_oficial": "Ocon", "numero": 31, "equipe": "Haas"},

    "oliver bearman": {"nome_oficial": "Bearman", "numero": 87, "equipe": "Haas"},
    "bearman": {"nome_oficial": "Bearman", "numero": 87, "equipe": "Haas"},

    "sergio perez": {"nome_oficial": "Perez", "numero": 11, "equipe": "Cadillac"},
    "perez": {"nome_oficial": "Perez", "numero": 11, "equipe": "Cadillac"},

    "valtteri bottas": {"nome_oficial": "Bottas", "numero": 77, "equipe": "Cadillac"},
    "bottas": {"nome_oficial": "Bottas", "numero": 77, "equipe": "Cadillac"}
}

PONTOS_F1 = {
    1: 25, 2: 18, 3: 15, 4: 12, 5: 10,
    6: 8, 7: 6, 8: 4, 9: 2, 10: 1
}


def cadastrar_corrida():
    print("\n" + "=" * 50)
    print("      CADASTRO DE CORRIDA      ")
    print("=" * 50)

    ano = int(input("Digite o ano da temporada (ex: 2026): "))
    corridas_feitas = banco.contar_corridas(ano)

    if corridas_feitas >= 24:
        print(f"\n⚠️ O campeonato de {ano} já atingiu o limite de 24 corridas!")
        exibir_campeoes(ano)
        return

    numero_corrida_atual = corridas_feitas + 1
    print(f"\n📌 Registrando a Corrida {numero_corrida_atual} de 24 do ano {ano}")

    circuito = input("Nome do circuito (ex: Interlagos): ").strip()

    # Verifica se o circuito já foi cadastrado nesse ano (evita duplicação)
    if banco.circuito_ja_cadastrado(ano, circuito):
        print(f"\n⚠️ O circuito '{circuito}' já foi cadastrado em {ano}! Cadastro cancelado.")
        return

    pole_position = input("Quem fez a Pole Position? ").strip()

    print("\n--- DIGITE A ORDEM DE CHEGADA (1º ao 22º Lugar) ---")
    resultados_corrida = []

    for posicao in range(1, 23):
        nome_input = input(f"Digite o piloto do {posicao}º lugar: ").strip()

        # Converte para minúsculas para padronizar a busca
        chave_busca = nome_input.lower()

        # Verifica se o piloto está no cadastro
        if chave_busca not in PILOTOS_TEMPORADA:
            print(f"⚠️  Piloto '{nome_input}' não encontrado no cadastro. Equipe ficará como 'Desconhecida'.")

        # Valor padrão padronizado com a chave "equipe" (corrigido)
        dados_cadastro = PILOTOS_TEMPORADA.get(chave_busca, {
            "nome_oficial": nome_input,
            "numero": 0,
            "equipe": "Desconhecida"
        })

        pontos = PONTOS_F1.get(posicao, 0)
        fez_pole = "Sim" if chave_busca == pole_position.lower() else "Não"

        registro = {
            'ano': ano,
            'circuito': circuito,
            'piloto': dados_cadastro['nome_oficial'],
            'equipe': dados_cadastro['equipe'],  # Chave padronizada para 'equipe'
            'numero': dados_cadastro['numero'],
            'posicao': posicao,
            'pontos': pontos,
            'pole_position': fez_pole
        }
        resultados_corrida.append(registro)

    banco.salvar_no_banco(resultados_corrida)
    exibir_campeoes(ano)


def exibir_campeoes(ano):
    """Exibe o líder/campeão de pilotos e de construtores."""
    piloto_campeao = banco.buscar_campeao_mundial(ano)
    equipe_campea = banco.buscar_equipe_campea(ano)

    print("\n" + "🏆" * 25)
    print(f"      CLASSIFICAÇÃO / CAMPEÕES DA TEMPORADA {ano}      ")
    print("=" * 50)

    if piloto_campeao and piloto_campeao[0] is not None:
        nome, equipe, pontos_piloto = piloto_campeao
        print(f"🥇 LÍDER / WORLD DRIVERS' CHAMPION (WC):")
        print(f"   Piloto: {nome}")
        print(f"   Equipe: {equipe}")
        print(f"   Pontos: {pontos_piloto} pts\n")
    else:
        print("Nenhum registro de piloto encontrado para esse ano.\n")

    if equipe_campea and equipe_campea[0] is not None:
        nome_eq, pontos_eq = equipe_campea
        print(f"🏆 LÍDER / WORLD CONSTRUCTORS' CHAMPION:")
        print(f"   Equipe: {nome_eq}")
        print(f"   Pontos: {pontos_eq} pts\n")
    else:
        print("Nenhum registro de equipe encontrado para esse ano.\n")


def menu():
    while True:
        print("\n=== MENU FÓRMULA 1 ===")
        print("1. Cadastrar Nova Corrida")
        print("2. Ver Classificação do Campeonato")
        print("3. Sair")

        opcao = input("Escolha uma opção (1-3): ")

        if opcao == "1":
            cadastrar_corrida()
        elif opcao == "2":
            ano = int(input("Digite o ano da temporada que deseja consultar: "))
            exibir_campeoes(ano)
        elif opcao == "3":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()