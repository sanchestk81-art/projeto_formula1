"""
data.py
-------
Script de carga de dados do portal 'Setor F1'.
Popula o PostgreSQL com:
- Usuários padrão (Admin e Cliente de exemplo com senhas hasheadas)
- Equipes completas (com modelo e imagem dos carros de corrida)
- Pilotos Titulares e Pilotos Reservas (com pontos na temporada e chances de título)
- Corridas Históricas com Pódio completo, Pole Position, Volta Rápida e Classificação completa
- Produtos da Loja com tags especiais (Mais Vendido, Edição Limitada, etc.) e Banners de Loja
- Banners rotativos dinâmicos para a Home e para a Loja Oficial
- Galeria de Fotos em alta definição do Paddock e Grandes Prêmios
"""

import os
import psycopg2
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash

# Carrega variáveis
load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "formula1")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "1234")


def popular_banco():
    print(" Conectando ao banco 'formula1' para alimentar os dados...")
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cur = conn.cursor()

        print(" Limpando dados anteriores com TRUNCATE CASCADE...")
        cur.execute("""
            TRUNCATE TABLE galeria, banners, pedidos, produtos, contatos, corridas, pilotos, noticias, equipes, usuarios RESTART IDENTITY CASCADE;
        """)

        # ----------------------------------------------------------------------
        # 1. USUÁRIOS (ADMIN E CLIENTE/FÃ)
        # ----------------------------------------------------------------------
        print(" Inserindo usuários padrão (Admin e Fã)...")
        usuarios_sql = """
            INSERT INTO usuarios (nome, email, senha_hash, tipo)
            VALUES (%s, %s, %s, %s)
            RETURNING id, email;
        """
        senha_admin = generate_password_hash("admin123")
        senha_cliente = generate_password_hash("fa123")

        cur.execute(usuarios_sql, ("Administrador Setor F1", "admin@setorf1.com", senha_admin, "admin"))
        admin_id = cur.fetchone()[0]

        cur.execute(usuarios_sql, ("Beatriz Fã de F1", "fa@setorf1.com", senha_cliente, "cliente"))
        cliente_id = cur.fetchone()[0]

        # ----------------------------------------------------------------------
        # 2. EQUIPES (COM MODELOS E FOTOS DOS CARROS)
        # ----------------------------------------------------------------------
        print(" Inserindo equipes...")
        equipes_sql = """
            INSERT INTO equipes (nome, nome_completo, pais_origem, sede, chefe_equipe, motor, titulos_construtores, ano_estreia, historia, logo_url, carro_modelo, carro_imagem_url, cor_primaria)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id, nome;
        """

        equipes_dados = [
            (
                "Ferrari",
                "Scuderia Ferrari HP",
                "Itália",
                "Maranello, Itália",
                "Frédéric Vasseur",
                "Ferrari",
                16,
                1950,
                "A mais lendária e tradicional equipe da história da Fórmula 1, presente desde 1950. Com 16 títulos de construtores e 15 de pilotos, a Ferrari carrega o peso e o amor dos Tifosi no mundo inteiro.",
                "https://upload.wikimedia.org/wikipedia/pt/thumb/d/d4/Scuderia_Ferrari_Logo.svg/500px-Scuderia_Ferrari_Logo.svg.png",
                "Ferrari SF-24",
                "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=1000&q=80",
                "#E80020"
            ),
            (
                "Red Bull Racing",
                "Oracle Red Bull Racing",
                "Áustria / Reino Unido",
                "Milton Keynes, Reino Unido",
                "Christian Horner",
                "Honda RBPT",
                6,
                2005,
                "Revolucionou a Fórmula 1 combinando engenharia de ponta de Adrian Newey com mentalidade vencedora. Dominou com Sebastian Vettel e quebrou recordes mundiais com Max Verstappen.",
                "https://upload.wikimedia.org/wikipedia/pt/thumb/5/52/Red_Bull_Racing_logo.svg/500px-Red_Bull_Racing_logo.svg.png",
                "Red Bull RB20",
                "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?auto=format&fit=crop&w=1000&q=80",
                "#0600EF"
            ),
            (
                "McLaren",
                "McLaren Formula 1 Team",
                "Reino Unido",
                "Woking, Reino Unido",
                "Andrea Stella",
                "Mercedes",
                8,
                1966,
                "Fundada por Bruce McLaren, construiu dinastias com Ayrton Senna, Alain Prost, Mika Häkkinen e Lewis Hamilton. Retornou às vitórias com a pintura Papaya de Lando Norris e Oscar Piastri.",
                "https://upload.wikimedia.org/wikipedia/pt/thumb/e/e0/McLaren_Formula_1_Team_Logo.svg/500px-McLaren_Formula_1_Team_Logo.svg.png",
                "McLaren MCL38",
                "https://images.unsplash.com/photo-1541348263662-e0c8de4259ba?auto=format&fit=crop&w=1000&q=80",
                "#FF8000"
            ),
            (
                "Mercedes",
                "Mercedes-AMG PETRONAS F1 Team",
                "Alemanha / Reino Unido",
                "Brackley, Reino Unido",
                "Toto Wolff",
                "Mercedes",
                8,
                1954,
                "As lendárias Flechas de Prata. Estabeleceu o recorde histórico de 8 títulos mundiais consecutivos de construtores (2014-2021) sob o comando de Toto Wolff.",
                "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Mercedes_AMG_Petronas_F1_Logo.svg/500px-Mercedes_AMG_Petronas_F1_Logo.svg.png",
                "Mercedes-AMG F1 W15",
                "https://images.unsplash.com/photo-1617788138017-80ad40651399?auto=format&fit=crop&w=1000&q=80",
                "#00D2BE"
            ),
            (
                "Aston Martin",
                "Aston Martin Aramco F1 Team",
                "Reino Unido",
                "Silverstone, Reino Unido",
                "Mike Krack",
                "Mercedes",
                0,
                1959,
                "O icônico verde britânico renasce com fábrica ultra avançada em Silverstone, unindo a genialidade de Fernando Alonso e investimentos de grande porte.",
                "https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Aston_Martin_Aramco_Cognizant_F1_Logo.svg/500px-Aston_Martin_Aramco_Cognizant_F1_Logo.svg.png",
                "Aston Martin AMR24",
                "https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?auto=format&fit=crop&w=1000&q=80",
                "#006F62"
            ),
            (
                "Williams",
                "Williams Racing",
                "Reino Unido",
                "Grove, Reino Unido",
                "James Vowles",
                "Mercedes",
                9,
                1977,
                "9 vezes campeã mundial de construtores, fundada por Sir Frank Williams. Histórico lendário com Senna, Piquet e Mansell, atualmente em reestruturação técnica moderna com James Vowles.",
                "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Williams_Racing_2020_Logo.svg/500px-Williams_Racing_2020_Logo.svg.png",
                "Williams FW46",
                "https://images.unsplash.com/photo-1542282088-72c9c27ed0cd?auto=format&fit=crop&w=1000&q=80",
                "#00A0DE"
            ),
            (
                "Alpine",
                "BWT Alpine F1 Team",
                "França / Reino Unido",
                "Enstone, Reino Unido",
                "Oliver Oakes",
                "Renault",
                2,
                1986,
                "Braço esportivo da Renault (bicampeã em 2005 e 2006). Protagonizou a histórica dobradinha francesa no pódio chuvoso de Interlagos 2024 com Esteban Ocon e Pierre Gasly.",
                "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Alpine_F1_Team_Logo.svg/500px-Alpine_F1_Team_Logo.svg.png",
                "Alpine A524",
                "https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=1000&q=80",
                "#0090FF"
            )
        ]

        equipe_id_map = {}
        for eq in equipes_dados:
            cur.execute(equipes_sql, eq)
            res = cur.fetchone()
            equipe_id_map[res[1]] = res[0]

        # ----------------------------------------------------------------------
        # 3. PILOTOS TITULARES E PILOTOS RESERVAS
        # ----------------------------------------------------------------------
        print(" Inserindo pilotos titulares e reservas...")
        pilotos_sql = """
            INSERT INTO pilotos (nome, numero, nacionalidade, pais_codigo, equipe_id, foto_url, como_entrou_f1, trajetoria_f1, titulos_mundiais, vitorias, podios, data_nascimento, ativo, papel_equipe, temporadas_ativas, pontos_temporada, chance_titulo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id, nome;
        """

        pilotos_dados = [
            # TITULARES
            (
                "Max Verstappen",
                1,
                "Holandesa",
                "nl",
                equipe_id_map["Red Bull Racing"],
                "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Max_Verstappen_2017_Malaysia_2.jpg/440px-Max_Verstappen_2017_Malaysia_2.jpg",
                "Prodígio do kart e F3 aos 16 anos, contratado pela Red Bull para a Toro Rosso em 2015, tornando-se o mais jovem da história a disputar um GP aos 17 anos.",
                "Venceu na estreia pela Red Bull na Espanha 2016 aos 18 anos. Campeão de 2021, bateu o recorde de 10 vitórias seguidas em 2023 e venceu o épico GP de São Paulo 2024 largando de 17º.",
                3, 63, 111, "1997-09-30", True, "titular", "2015 - Atual", 393, 72.5
            ),
            (
                "Lando Norris",
                4,
                "Britânica",
                "gb",
                equipe_id_map["McLaren"],
                "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Lando_Norris_2022_Bahrain_GP_%28cropped%29.jpg/440px-Lando_Norris_2022_Bahrain_GP_%28cropped%29.jpg",
                "Campeão da F3 Europeia e vice da F2, piloto da academia júnior da McLaren, promovido a titular em 2019 com apenas 19 anos.",
                "1º pódio na Áustria 2020 com o famoso 'Scenario 7'. Liderou a reconstrução da McLaren, conquistou vitórias em Miami, Holanda e Singapura, disputando o título mundial.",
                0, 4, 29, "1999-11-13", True, "titular", "2019 - Atual", 331, 23.5
            ),
            (
                "Charles Leclerc",
                16,
                "Monegasca",
                "mc",
                equipe_id_map["Ferrari"],
                "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Charles_Leclerc%2C_British_GP_2022_%28cropped%29.jpg/440px-Charles_Leclerc%2C_British_GP_2022_%28cropped%29.jpg",
                "Destaque da Ferrari Driver Academy, campeão consecutivo da GP3 em 2016 e Fórmula 2 em 2017, estreou na F1 em 2018 pela Sauber.",
                "Promovido para a Ferrari em 2019 aos 21 anos, venceu em Spa e Monza superando Sebastian Vettel. Vencedor do Grande Prêmio de Mônaco em casa.",
                0, 8, 42, "1997-10-16", True, "titular", "2018 - Atual", 307, 4.0
            ),
            (
                "Oscar Piastri",
                81,
                "Australiana",
                "au",
                equipe_id_map["McLaren"],
                "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Oscar_Piastri_2023_British_GP_%28cropped%29.jpg/440px-Oscar_Piastri_2023_British_GP_%28cropped%29.jpg",
                "Três títulos consecutivos como estreante: Fórmula Renault (2019), Fórmula 3 (2020) e Fórmula 2 (2021).",
                "Estreou pela McLaren em 2023 com compostura impecável, vencendo a corrida Sprint no Catar e vitórias em GPs na Hungria e Azerbaijão.",
                0, 2, 10, "2001-04-06", True, "titular", "2023 - Atual", 262, 0.0
            ),
            (
                "George Russell",
                63,
                "Britânica",
                "gb",
                equipe_id_map["Mercedes"],
                "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/George_Russell_2022_Bahrain_GP_%28cropped%29.jpg/440px-George_Russell_2022_Bahrain_GP_%28cropped%29.jpg",
                "Campeão da GP3 e F2, piloto da Mercedes Academy que estreou pela Williams em 2019 ganhando o apelido de 'Mr. Saturday'.",
                "Promovido para a equipe principal da Mercedes em 2022, venceu o GP de São Paulo e é a liderança técnica do time alemão.",
                0, 3, 15, "1998-02-15", True, "titular", "2019 - Atual", 192, 0.0
            ),
            (
                "Lewis Hamilton",
                44,
                "Britânica",
                "gb",
                equipe_id_map["Ferrari"],
                "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Lewis_Hamilton_2022_Bahrain_GP_%28cropped%29.jpg/440px-Lewis_Hamilton_2022_Bahrain_GP_%28cropped%29.jpg",
                "Apoiado por Ron Dennis na McLaren desde os 13 anos, estreou na McLaren em 2007 disputando o título até a prova final.",
                "7 vezes campeão mundial, mais de 100 vitórias e 100 poles. Conquistou 6 títulos na Mercedes e assinou com a Ferrari para buscar o sonhado 8º campeonato.",
                7, 105, 201, "1985-01-07", True, "titular", "2007 - Atual", 190, 0.0
            ),
            (
                "Fernando Alonso",
                14,
                "Espanhola",
                "es",
                equipe_id_map["Aston Martin"],
                "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Fernando_Alonso_2022_Bahrain_GP_%28cropped%29.jpg/440px-Fernando_Alonso_2022_Bahrain_GP_%28cropped%29.jpg",
                "Estreou em 2001 pela Minardi mostrando talento genial.",
                "Bicampeão mundial consecutivo (2005 e 2006) quebrando o império de Michael Schumacher. Mais de 400 GPs disputados e múltiplos pódios na Aston Martin.",
                2, 32, 106, "1981-07-29", True, "titular", "2001 - Atual", 62, 0.0
            ),
            (
                "Gabriel Bortoleto",
                5,
                "Brasileira",
                "br",
                equipe_id_map["Williams"],
                "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Gabriel_Bortoleto_2024_Spielberg_F2.jpg/440px-Gabriel_Bortoleto_2024_Spielberg_F2.jpg",
                "Campeão da FIA F3 como estreante em 2023 e vencedor espetacular na Fórmula 2 em 2024 (largou em último e venceu em Monza), agenciado por Fernando Alonso.",
                "Marca o aguardado retorno do Brasil ao grid titular da Fórmula 1, carregando o legado verde e amarelo e grande entusiasmo internacional.",
                0, 0, 0, "2004-10-14", True, "titular", "2025 - Atual", 0, 0.0
            ),

            # PILOTOS RESERVAS
            (
                "Oliver Bearman",
                38,
                "Britânica",
                "gb",
                equipe_id_map["Ferrari"],
                "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Oliver_Bearman_2024_Spielberg_F2.jpg/440px-Oliver_Bearman_2024_Spielberg_F2.jpg",
                "Destaque da Ferrari Driver Academy, estreou de emergência na F1 aos 18 anos no GP da Arábia Saudita pontuando com bravura.",
                "Piloto reserva oficial da Scuderia Ferrari e titular confirmado para as próximas temporadas.",
                0, 0, 0, "2005-05-08", True, "reserva", "2024 - Atual", 7, 0.0
            ),
            (
                "Liam Lawson",
                30,
                "Neozelandesa",
                "nz",
                equipe_id_map["Red Bull Racing"],
                "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Liam_Lawson_2022_Spielberg_F2.jpg/440px-Liam_Lawson_2022_Spielberg_F2.jpg",
                "Piloto do programa Red Bull Junior Team com passagens vitoriosas na Super Formula e F2.",
                "Piloto de desenvolvimento e reserva oficial da Red Bull Racing.",
                0, 0, 0, "2002-02-11", True, "reserva", "2023 - Atual", 4, 0.0
            ),
            (
                "Mick Schumacher",
                47,
                "Alemã",
                "de",
                equipe_id_map["Mercedes"],
                "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Mick_Schumacher_2022_Bahrain_GP_%28cropped%29.jpg/440px-Mick_Schumacher_2022_Bahrain_GP_%28cropped%29.jpg",
                "Campeão da F3 Europeia e campeão da Fórmula 2, filho do heptacampeão mundial Michael Schumacher.",
                "Piloto reserva e de testes da Mercedes-AMG PETRONAS.",
                0, 0, 0, "1999-03-22", True, "reserva", "2021 - Atual", 0, 0.0
            ),

            # HISTÓRICOS (Para corridas antigas e consultas)
            (
                "Valtteri Bottas",
                77,
                "Finlandesa",
                "fi",
                equipe_id_map["Mercedes"],
                "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Valtteri_Bottas_2019_Malaysia.jpg/440px-Valtteri_Bottas_2019_Malaysia.jpg",
                "Campeão da GP3, estreou na Williams em 2013 e correu pela Mercedes conquistando 10 vitórias.",
                "Venceu a 1ª corrida de 2020 na Áustria liderando de ponta a ponta. 67 pódios na carreira.",
                0, 10, 67, "1989-08-28", False, "titular", "2013 - 2024", 0, 0.0
            ),
            (
                "Sebastian Vettel",
                5,
                "Alemã",
                "de",
                equipe_id_map["Ferrari"],
                "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Sebastian_Vettel_2019_Malaysia.jpg/440px-Sebastian_Vettel_2019_Malaysia.jpg",
                "Tetracampeão mundial consecutivo com a Red Bull (2010-2013).",
                "53 vitórias e 122 pódios na Fórmula 1.",
                4, 53, 122, "1987-07-03", False, "titular", "2007 - 2022", 0, 0.0
            ),
            (
                "Ayrton Senna",
                12,
                "Brasileira",
                "br",
                equipe_id_map["McLaren"],
                "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Ayrton_Senna_8%2C_1989.jpg/440px-Ayrton_Senna_8%2C_1989.jpg",
                "Tricampeão mundial (1988, 1990 e 1991), 41 vitórias e 65 poles.",
                "Considerado a maior lenda pura do automobilismo mundial.",
                3, 41, 80, "1960-03-21", False, "titular", "1984 - 1994", 0, 0.0
            )
        ]

        piloto_id_map = {}
        for p in pilotos_dados:
            cur.execute(pilotos_sql, p)
            res = cur.fetchone()
            piloto_id_map[res[1]] = res[0]

        # ----------------------------------------------------------------------
        # 4. CORRIDAS COM POLE, PÓDIO COMPLETO, VOLTA RÁPIDA E CLASSIFICAÇÃO
        # ----------------------------------------------------------------------
        print(" Inserindo corridas detalhadas...")
        corridas_sql = """
            INSERT INTO corridas (ano, rodada, nome_gp, circuito, pais, pais_codigo, cidade, data_corrida, status,
                                  pole_position_piloto_id, pole_position_tempo,
                                  vencedor_piloto_id, vencedor_equipe,
                                  segundo_piloto_id, segundo_lugar,
                                  terceiro_piloto_id, terceiro_lugar,
                                  volta_rapida_piloto_id, volta_mais_rapida,
                                  noticias_resumo, classificacao_detalhada, imagem_circuito_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id, nome_gp;
        """

        corridas_dados = [
            # 1ª CORRIDA DE 2020 (Áustria)
            (
                2020,
                1,
                "Grande Prêmio da Áustria 2020",
                "Red Bull Ring",
                "Áustria",
                "at",
                "Spielberg",
                "2020-07-05",
                "concluida",
                piloto_id_map["Valtteri Bottas"],
                "1:02.939 (Mercedes)",
                piloto_id_map["Valtteri Bottas"],
                "Mercedes",
                piloto_id_map["Charles Leclerc"],
                "Charles Leclerc (Ferrari)",
                piloto_id_map["Lando Norris"],
                "Lando Norris (McLaren)",
                piloto_id_map["Lando Norris"],
                "Lando Norris (1:07.475 na volta 71)",
                "A corrida de abertura da temporada de 2020 foi histórica e imprevisível. Valtteri Bottas largou na pole e controlou os múltiplos Safety Cars para vencer pela Mercedes. A prova teve 9 abandonos e um final dramático: Hamilton foi punido em 5s e Lando Norris cravou a volta mais rápida na volta final ('Scenario 7') garantindo seu 1º pódio da carreira!",
                "1º Valtteri Bottas (Mercedes) - 1:30:55.739\n2º Charles Leclerc (Ferrari) +2.700s\n3º Lando Norris (McLaren) +5.491s\n4º Lewis Hamilton (Mercedes) +5.619s (penalizado)\n5º Carlos Sainz (McLaren) +8.903s\n6º Sergio Pérez (Racing Point) +15.058s\n7º Pierre Gasly (AlphaTauri) +16.682s\n8º Esteban Ocon (Renault) +17.456s\n9º Antonio Giovinazzi (Alfa Romeo) +21.146s\n10º Sebastian Vettel (Ferrari) +24.545s",
                "https://images.unsplash.com/photo-1541348263662-e0c8de4259ba?auto=format&fit=crop&w=1000&q=80"
            ),
            # GP DE SÃO PAULO 2024 (Interlagos Corrigido)
            (
                2024,
                21,
                "Grande Prêmio de São Paulo 2024",
                "Autódromo José Carlos Pace (Interlagos)",
                "Brasil",
                "br",
                "São Paulo",
                "2024-11-03",
                "concluida",
                piloto_id_map["Lando Norris"],
                "1:23.405 (McLaren)",
                piloto_id_map["Max Verstappen"],
                "Red Bull Racing",
                None,
                "Esteban Ocon (Alpine)",
                None,
                "Pierre Gasly (Alpine)",
                piloto_id_map["Max Verstappen"],
                "Max Verstappen (1:20.472)",
                "Uma das maiores atuações da história da F1 sob tempestade em Interlagos. Max Verstappen largou em 17º e realizou ultrapassagens inacreditáveis, vencendo com mais de 19s de vantagem e 17 voltas mais rápidas. A Alpine fez história colocando Esteban Ocon em 2º e Pierre Gasly em 3º no pódio duplo!",
                "1º Max Verstappen (Red Bull Racing) - 2:06:54.430 (Largou de 17º)\n2º Esteban Ocon (Alpine) +19.477s\n3º Pierre Gasly (Alpine) +22.532s\n4º George Russell (Mercedes) +23.265s\n5º Charles Leclerc (Ferrari) +30.177s\n6º Lando Norris (McLaren) +31.372s\n7º Yuki Tsunoda (RB) +42.056s\n8º Oscar Piastri (McLaren) +44.943s\n9º Liam Lawson (RB) +50.452s\n10º Lewis Hamilton (Mercedes) +50.768s",
                "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=1000&q=80"
            ),
            # PRÓXIMA CORRIDA
            (
                2026,
                22,
                "Grande Prêmio de Las Vegas",
                "Circuito de Rua de Las Vegas (The Strip)",
                "Estados Unidos",
                "us",
                "Las Vegas",
                "2026-11-23",
                "proxima",
                None, None, None, None, None, None, None, None, None, None,
                "A prova noturna mais veloz da temporada, percorrendo a famosa 'The Strip' com os carros ultrapassando 350 km/h sob o frio do deserto.",
                "Grid de largada a ser definido na sessão de classificação oficial de sábado.",
                "https://images.unsplash.com/photo-1581351721010-8cf859cb14a4?auto=format&fit=crop&w=1000&q=80"
            )
        ]

        for c in corridas_dados:
            cur.execute(corridas_sql, c)

        # ----------------------------------------------------------------------
        # 5. NOTÍCIAS
        # ----------------------------------------------------------------------
        print(" Inserindo notícias...")
        noticias_sql = """
            INSERT INTO noticias (titulo, subtitulo, conteudo, data_publicacao, categoria, imagem_url, autor, destaque, no_banner, criado_por_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        noticias_dados = [
            (
                "Setor F1: Gabriel Bortoleto confirma o renascimento do Brasil no grid",
                "Com atuações magistrais e o apoio de Fernando Alonso, o jovem paulista assume cockpit titular e reacende a paixão nacional.",
                "O automobilismo brasileiro celebra uma conquista monumental. Gabriel Bortoleto, campeão da Fórmula 3 e destaque absoluto da Fórmula 2, garantiu oficialmente seu assento como piloto titular na Fórmula 1.\n\nCom apenas 20 anos, Bortoleto impressionou o paddock internacional pela maturidade com que gerencia corridas complexas e sua velocidade em classificação. Agenciado pelo bicampeão mundial Fernando Alonso, o brasileiro declarou: 'É a realização de um sonho de infância que começou nos karts do Brasil. Sei da responsabilidade que carrego ao representar as cores do nosso país na maior categoria do mundo e vou dar tudo de mim'.",
                "2026-11-10",
                "Mercado & Brasil",
                "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=1200&q=80",
                "Redação Setor F1",
                True,
                True,
                admin_id
            ),
            (
                "Guerra de Construtores: McLaren, Ferrari e Red Bull travam duelo milimétrico",
                "Com menos de 40 pontos separando os líderes, a disputa de equipes entra na reta final com atualizações técnicas arriscadas.",
                "A temporada atual consolidou-se como uma das mais equilibradas e espetaculares das últimas décadas na Fórmula 1. McLaren, Ferrari e Red Bull chegam às etapas decisivas disputando curva a curva o cobiçado troféu de Campeã Mundial de Construtores.",
                "2026-11-09",
                "Campeonato",
                "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?auto=format&fit=crop&w=1200&q=80",
                "Carlos Silva - Setor F1",
                False,
                True,
                admin_id
            )
        ]

        for n in noticias_dados:
            cur.execute(noticias_sql, n)

        # ----------------------------------------------------------------------
        # 6. PRODUTOS DA LOJA (COM BANNERS DE LOJA)
        # ----------------------------------------------------------------------
        print(" Inserindo produtos da loja com tags e banners...")
        produtos_sql = """
            INSERT INTO produtos (nome, categoria, equipe_id, preco, descricao, imagem_url, estoque, tag, destaque, no_banner_home, no_banner_loja)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id, nome;
        """

        produtos_dados = [
            (
                "Boné Oficial Scuderia Ferrari HP 2026",
                "Bonés",
                equipe_id_map["Ferrari"],
                289.90,
                "Boné oficial da equipe italiana em tecido respirável premium, aba curva com detalhe tricolor e escudo Ferrari bordado em alta definição.",
                "https://images.unsplash.com/photo-1588850561407-ed78c282e89b?auto=format&fit=crop&w=800&q=80",
                45,
                "Mais Vendido",
                True,
                True,
                True
            ),
            (
                "Miniatura Capacete Ayrton Senna 1993 Escala 1:5",
                "Miniaturas",
                equipe_id_map["McLaren"],
                390.00,
                "Réplica artesanal oficial do capacete amarelo mais icônico da história do esporte, com viseira móvel e pedestal com placa metálica comemorativa.",
                "https://images.unsplash.com/photo-1578632767115-351597cf2477?auto=format&fit=crop&w=800&q=80",
                8,
                "Edição Limitada",
                True,
                True,
                True
            ),
            (
                "Camiseta Red Bull Racing World Champion",
                "Camisetas",
                equipe_id_map["Red Bull Racing"],
                349.90,
                "Camiseta comemorativa confeccionada em algodão orgânico premium com estampa emborrachada fosca dos títulos mundiais e patrocinadores oficiais.",
                "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=800&q=80",
                30,
                "Nova Coleção",
                True,
                False,
                True
            ),
            (
                "Miniatura McLaren MCL38 Lando Norris 1:43",
                "Miniaturas",
                equipe_id_map["McLaren"],
                420.00,
                "Miniatura colecionável die-cast em escala 1:43 com pintura automotiva Papaya idêntica ao carro real, pneus de composto macio e base de acrílico expositora.",
                "https://images.unsplash.com/photo-1594787318286-3d835c1d207f?auto=format&fit=crop&w=800&q=80",
                15,
                "Exclusivo",
                False,
                False,
                False
            ),
            (
                "Jaqueta Corta-Vento Mercedes-AMG PETRONAS",
                "Jaquetas",
                equipe_id_map["Mercedes"],
                699.00,
                "Jaqueta impermeável corta-vento com capuz embutido, detalhes no clássico verde água Petronas e zíper selado contra água e vento.",
                "https://images.unsplash.com/photo-1551028719-00167b16eac5?auto=format&fit=crop&w=800&q=80",
                20,
                "Nova Coleção",
                False,
                False,
                False
            )
        ]

        produto_id_map = {}
        for pr in produtos_dados:
            cur.execute(produtos_sql, pr)
            res = cur.fetchone()
            produto_id_map[res[1]] = res[0]

        # ----------------------------------------------------------------------
        # 7. BANNERS ROTATIVOS (HOME E LOJA)
        # ----------------------------------------------------------------------
        print(" Inserindo banners da home e da loja...")
        banners_sql = """
            INSERT INTO banners (titulo, subtitulo, imagem_url, link_url, tag_destaque, local_exibicao, produto_id, ordem, ativo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        banners_dados = [
            # BANNERS DA HOME
            (
                "Gabriel Bortoleto na F1: O Brasil de Volta ao Grid!",
                "Acompanhe a trajetória do piloto paulista rumo à elite do automobilismo mundial.",
                "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=1400&q=80",
                "/pilotos",
                "NOVIDADE NO GRID",
                "home",
                None,
                1,
                True
            ),
            (
                "Duelo pelo Título Mundial: Verstappen vs Norris",
                "A disputa milimétrica de pontos na reta final da temporada. Confira as chances de cada piloto!",
                "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?auto=format&fit=crop&w=1400&q=80",
                "/corridas",
                "DISPUTA DO CAMPEONATO",
                "home",
                None,
                2,
                True
            ),
            # BANNERS ESPECIAIS DA LOJA OFICIAL (COM FOTOS E BOTÕES DE COMPRA)
            (
                "Boné Oficial Scuderia Ferrari HP • R$ 289,90",
                "Edição especial da equipe italiana com escudo bordado e acabamento premium para os Tifosi.",
                "https://images.unsplash.com/photo-1588850561407-ed78c282e89b?auto=format&fit=crop&w=1400&q=80",
                "/loja",
                "MAIS VENDIDO",
                "loja",
                produto_id_map["Boné Oficial Scuderia Ferrari HP 2026"],
                1,
                True
            ),
            (
                "Capacete Ayrton Senna 1993 • Edição Limitada • R$ 390,00",
                "Réplica oficial de colecionador em escala 1:5 do capacete mais icônico de todos os tempos.",
                "https://images.unsplash.com/photo-1578632767115-351597cf2477?auto=format&fit=crop&w=1400&q=80",
                "/loja",
                "EDIÇÃO LIMITADA",
                "loja",
                produto_id_map["Miniatura Capacete Ayrton Senna 1993 Escala 1:5"],
                2,
                True
            ),
            (
                "Camiseta Red Bull Racing World Champion • R$ 349,90",
                "Vista as cores do time campeão mundial com tecido dry-fit ultra confortável.",
                "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=1400&q=80",
                "/loja",
                "NOVA COLEÇÃO",
                "loja",
                produto_id_map["Camiseta Red Bull Racing World Champion"],
                3,
                True
            )
        ]

        for b in banners_dados:
            cur.execute(banners_sql, b)

        # ----------------------------------------------------------------------
        # 8. GALERIA DE FOTOS DO PADDOCK E CORRIDAS
        # ----------------------------------------------------------------------
        print(" Inserindo fotos na galeria...")
        galeria_sql = """
            INSERT INTO galeria (titulo, categoria, imagem_url, descricao)
            VALUES (%s, %s, %s, %s);
        """

        galeria_dados = [
            (
                "Chuva Épica em Interlagos",
                "Chuva & Emoção",
                "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=1200&q=80",
                "Monopostos desafiando o asfalto encharcado na Curva do Sol diante das arquibancadas lotadas em São Paulo."
            ),
            (
                "Celebração de Pódio e Champanhe",
                "Pódio",
                "https://images.unsplash.com/photo-1541348263662-e0c8de4259ba?auto=format&fit=crop&w=1200&q=80",
                "A tradicional festa no degrau mais alto do pódio com troféus e banho de champanhe entre os vencedores."
            ),
            (
                "Pit Stop em Menos de 2 Segundos",
                "Bastidores",
                "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?auto=format&fit=crop&w=1200&q=80",
                "Sincronia milimétrica de mais de 20 mecânicos trocando os quatro pneus na velocidade da luz."
            ),
            (
                "Velocidade Máxima na Reta de Yas Marina",
                "Carros",
                "https://images.unsplash.com/photo-1617788138017-80ad40651399?auto=format&fit=crop&w=1200&q=80",
                "Carros a mais de 340 km/h sob os holofotes do crepúsculo de Abu Dhabi."
            ),
            (
                "Concentração Total no Cockpit",
                "Paddock",
                "https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?auto=format&fit=crop&w=1200&q=80",
                "Olhar fixo na largada através da viseira escura momentos antes de apagarem as luzes vermelhas."
            ),
            (
                "Engenharia de Precisão e Fibra de Carbono",
                "Carros",
                "https://images.unsplash.com/photo-1542282088-72c9c27ed0cd?auto=format&fit=crop&w=1200&q=80",
                "Detalhe aerodinâmico dos dutos de freio e asas dianteiras flexíveis de última geração."
            )
        ]

        for g in galeria_dados:
            cur.execute(galeria_sql, g)

        # ----------------------------------------------------------------------
        # 9. CONTATOS DE EXEMPLO
        # ----------------------------------------------------------------------
        print(" Inserindo feedbacks...")
        contatos_sql = """
            INSERT INTO contatos (nome, email, tipo_feedback, assunto, mensagem)
            VALUES (%s, %s, %s, %s, %s);
        """
        cur.execute(contatos_sql, (
            "Juliana Rocha",
            "juliana.f1@email.com",
            "Elogio",
            "Setor F1 está incrível!",
            "Adorei o banner da loja com os botões de adicionar ao carrinho e a galeria de fotos do paddock!"
        ))

        conn.commit()
        cur.close()
        conn.close()

        print("\n [SUCESSO] Todos os dados foram inseridos com êxito!")

    except psycopg2.Error as erro:
        print(f"\n[ERRO] Falha ao popular dados: {erro}")
        raise erro


if __name__ == "__main__":
    popular_banco()
