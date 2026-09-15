import banco

# HISTÓRICO COMPLETO DA TEMPORADA DE 2020 (17 CORRIDAS)
corridas_2020 = [
    # Etapa 1: Áustria (Spielberg)
    {"ano": 2020, "circuito": "Spielberg", "piloto": "Bottas", "equipe": "Mercedes", "numero": 77, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2020, "circuito": "Spielberg", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 2: Estíria (Spielberg)
    {"ano": 2020, "circuito": "Estiria", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2020, "circuito": "Estiria", "piloto": "Bottas", "equipe": "Mercedes", "numero": 77, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 3: Hungria (Hungaroring)
    {"ano": 2020, "circuito": "Hungaroring", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2020, "circuito": "Hungaroring", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 4: Grã-Bretanha (Silverstone)
    {"ano": 2020, "circuito": "Silverstone", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2020, "circuito": "Silverstone", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 5: GP dos 70 Anos (Silverstone)
    {"ano": 2020, "circuito": "Silverstone (70 Anos)", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2020, "circuito": "Silverstone (70 Anos)", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 2, "pontos": 18, "pole_position": "Sim"},

    # Etapa 6: Espanha (Barcelona)
    {"ano": 2020, "circuito": "Barcelona", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2020, "circuito": "Barcelona", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 7: Bélgica (Spa-Francorchamps)
    {"ano": 2020, "circuito": "Spa-Francorchamps", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2020, "circuito": "Spa-Francorchamps", "piloto": "Bottas", "equipe": "Mercedes", "numero": 77, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 8: Itália (Monza)
    {"ano": 2020, "circuito": "Monza", "piloto": "Gasly", "equipe": "AlphaTauri", "numero": 10, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2020, "circuito": "Monza", "piloto": "Sainz", "equipe": "McLaren", "numero": 55, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 9: Toscana (Mugello)
    {"ano": 2020, "circuito": "Mugello", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2020, "circuito": "Mugello", "piloto": "Bottas", "equipe": "Mercedes", "numero": 77, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 10: Rússia (Sochi)
    {"ano": 2020, "circuito": "Sochi", "piloto": "Bottas", "equipe": "Mercedes", "numero": 77, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2020, "circuito": "Sochi", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 11: Eifel (Nürburgring)
    {"ano": 2020, "circuito": "Nurburgring", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2020, "circuito": "Nurburgring", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 12: Portugal (Portimão)
    {"ano": 2020, "circuito": "Portimao", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2020, "circuito": "Portimao", "piloto": "Bottas", "equipe": "Mercedes", "numero": 77, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 13: Emília-Romanha (Imola)
    {"ano": 2020, "circuito": "Imola", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2020, "circuito": "Imola", "piloto": "Bottas", "equipe": "Mercedes", "numero": 77, "posicao": 2, "pontos": 18, "pole_position": "Sim"},

    # Etapa 14: Turquia (Istambul)
    {"ano": 2020, "circuito": "Istambul", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2020, "circuito": "Istambul", "piloto": "Perez", "equipe": "Racing Point", "numero": 11, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 15: Bahrein (Sakhir)
    {"ano": 2020, "circuito": "Sakhir", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2020, "circuito": "Sakhir", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 16: Sakhir (Circuito Anel Externo)
    {"ano": 2020, "circuito": "Sakhir Anel Externo", "piloto": "Perez", "equipe": "Racing Point", "numero": 11, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2020, "circuito": "Sakhir Anel Externo", "piloto": "Ocon", "equipe": "Renault", "numero": 31, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 17: Abu Dhabi (Yas Marina)
    {"ano": 2020, "circuito": "Yas Marina", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2020, "circuito": "Yas Marina", "piloto": "Bottas", "equipe": "Mercedes", "numero": 77, "posicao": 2, "pontos": 18, "pole_position": "Não"}
]

if __name__ == "__main__":
    print("Iniciando a inserção de todas as 17 corridas de 2020 no SQLite...")
    banco.salvar_no_banco(corridas_2020)
    print("✅ Carga da Temporada 2020 concluída com sucesso!")

#corridas de 2021

import banco

# HISTÓRICO COMPLETO DA TEMPORADA DE 2021 (22 CORRIDAS)
corridas_2021 = [
    # Etapa 1: Bahrein (Sakhir)
    {"ano": 2021, "circuito": "Sakhir", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2021, "circuito": "Sakhir", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 2, "pontos": 18, "pole_position": "Sim"},

    # Etapa 2: Emília-Romanha (Imola)
    {"ano": 2021, "circuito": "Imola", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2021, "circuito": "Imola", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 2, "pontos": 18, "pole_position": "Sim"},

    # Etapa 3: Portugal (Portimão)
    {"ano": 2021, "circuito": "Portimao", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2021, "circuito": "Portimao", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 4: Espanha (Barcelona)
    {"ano": 2021, "circuito": "Barcelona", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2021, "circuito": "Barcelona", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 5: Mônaco (Monte Carlo)
    {"ano": 2021, "circuito": "Monaco", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2021, "circuito": "Monaco", "piloto": "Sainz", "equipe": "Ferrari", "numero": 55, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 6: Azerbaijão (Baku)
    {"ano": 2021, "circuito": "Baku", "piloto": "Perez", "equipe": "Red Bull Racing", "numero": 11, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2021, "circuito": "Baku", "piloto": "Vettel", "equipe": "Aston Martin", "numero": 5, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 7: França (Paul Ricard)
    {"ano": 2021, "circuito": "Paul Ricard", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2021, "circuito": "Paul Ricard", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 8: Estíria (Spielberg)
    {"ano": 2021, "circuito": "Estiria", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2021, "circuito": "Estiria", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 9: Áustria (Spielberg)
    {"ano": 2021, "circuito": "Spielberg", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2021, "circuito": "Spielberg", "piloto": "Bottas", "equipe": "Mercedes", "numero": 77, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 10: Grã-Bretanha (Silverstone)
    {"ano": 2021, "circuito": "Silverstone", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2021, "circuito": "Silverstone", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 11: Hungria (Hungaroring)
    {"ano": 2021, "circuito": "Hungaroring", "piloto": "Ocon", "equipe": "Alpine", "numero": 31, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2021, "circuito": "Hungaroring", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 2, "pontos": 18, "pole_position": "Sim"},

    # Etapa 12: Bélgica (Spa-Francorchamps)
    {"ano": 2021, "circuito": "Spa-Francorchamps", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2021, "circuito": "Spa-Francorchamps", "piloto": "Russell", "equipe": "Williams", "numero": 63, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 13: Holanda (Zandvoort)
    {"ano": 2021, "circuito": "Zandvoort", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2021, "circuito": "Zandvoort", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 14: Itália (Monza)
    {"ano": 2021, "circuito": "Monza", "piloto": "Ricciardo", "equipe": "McLaren", "numero": 3, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2021, "circuito": "Monza", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 15: Rússia (Sochi)
    {"ano": 2021, "circuito": "Sochi", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2021, "circuito": "Sochi", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 16: Turquia (Istambul)
    {"ano": 2021, "circuito": "Istambul", "piloto": "Bottas", "equipe": "Mercedes", "numero": 77, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2021, "circuito": "Istambul", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 17: Estados Unidos (Austin)
    {"ano": 2021, "circuito": "Austin", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2021, "circuito": "Austin", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 18: Cidade do México (Hermanos Rodríguez)
    {"ano": 2021, "circuito": "Cidade do Mexico", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2021, "circuito": "Cidade do Mexico", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 19: São Paulo (Interlagos)
    {"ano": 2021, "circuito": "Interlagos", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2021, "circuito": "Interlagos", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 2, "pontos": 18, "pole_position": "Sim"},

    # Etapa 20: Catar (Losail)
    {"ano": 2021, "circuito": "Losail", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2021, "circuito": "Losail", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 21: Arábia Saudita (Jidá)
    {"ano": 2021, "circuito": "Jida", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2021, "circuito": "Jida", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 22: Abu Dhabi (Yas Marina)
    {"ano": 2021, "circuito": "Yas Marina", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 33, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2021, "circuito": "Yas Marina", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 2, "pontos": 18, "pole_position": "Não"}
]

if __name__ == "__main__":
    print("Iniciando a inserção de todas as 22 corridas de 2021 no SQLite...")
    banco.salvar_no_banco(corridas_2021)
    print("✅ Carga da Temporada 2021 concluída com sucesso!")


## TEMPORADA DE 2022

# --- TEMPORADA 2022 ---
corridas_2022 = [
    # Etapa 1: Bahrein (Sakhir)
    {"ano": 2022, "circuito": "Sakhir", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2022, "circuito": "Sakhir", "piloto": "Sainz", "equipe": "Ferrari", "numero": 55, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 2: Arábia Saudita (Jidá)
    {"ano": 2022, "circuito": "Jida", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2022, "circuito": "Jida", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 3: Austrália (Melbourne)
    {"ano": 2022, "circuito": "Albert Park", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2022, "circuito": "Albert Park", "piloto": "Perez", "equipe": "Red Bull Racing", "numero": 11, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 4: Emília-Romanha (Imola)
    {"ano": 2022, "circuito": "Imola", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2022, "circuito": "Imola", "piloto": "Perez", "equipe": "Red Bull Racing", "numero": 11, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 5: Miami
    {"ano": 2022, "circuito": "Miami", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2022, "circuito": "Miami", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 2, "pontos": 18, "pole_position": "Sim"},

    # Etapa 6: Espanha (Barcelona)
    {"ano": 2022, "circuito": "Barcelona", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2022, "circuito": "Barcelona", "piloto": "Perez", "equipe": "Red Bull Racing", "numero": 11, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 7: Mônaco (Monte Carlo)
    {"ano": 2022, "circuito": "Monaco", "piloto": "Perez", "equipe": "Red Bull Racing", "numero": 11, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2022, "circuito": "Monaco", "piloto": "Sainz", "equipe": "Ferrari", "numero": 55, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 8: Azerbaijão (Baku)
    {"ano": 2022, "circuito": "Baku", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2022, "circuito": "Baku", "piloto": "Perez", "equipe": "Red Bull Racing", "numero": 11, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 9: Canadá (Montreal)
    {"ano": 2022, "circuito": "Montreal", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2022, "circuito": "Montreal", "piloto": "Sainz", "equipe": "Ferrari", "numero": 55, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 10: Grã-Bretanha (Silverstone)
    {"ano": 2022, "circuito": "Silverstone", "piloto": "Sainz", "equipe": "Ferrari", "numero": 55, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2022, "circuito": "Silverstone", "piloto": "Perez", "equipe": "Red Bull Racing", "numero": 11, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 11: Áustria (Spielberg)
    {"ano": 2022, "circuito": "Spielberg", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2022, "circuito": "Spielberg", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 2, "pontos": 18, "pole_position": "Sim"},

    # Etapa 12: França (Paul Ricard)
    {"ano": 2022, "circuito": "Paul Ricard", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2022, "circuito": "Paul Ricard", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 13: Hungria (Hungaroring)
    {"ano": 2022, "circuito": "Hungaroring", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2022, "circuito": "Hungaroring", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 14: Bélgica (Spa-Francorchamps)
    {"ano": 2022, "circuito": "Spa-Francorchamps", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2022, "circuito": "Spa-Francorchamps", "piloto": "Perez", "equipe": "Red Bull Racing", "numero": 11, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 15: Holanda (Zandvoort)
    {"ano": 2022, "circuito": "Zandvoort", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2022, "circuito": "Zandvoort", "piloto": "Russell", "equipe": "Mercedes", "numero": 63, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 16: Itália (Monza)
    {"ano": 2022, "circuito": "Monza", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2022, "circuito": "Monza", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 2, "pontos": 18, "pole_position": "Sim"},

    # Etapa 17: Singapura (Marina Bay)
    {"ano": 2022, "circuito": "Marina Bay", "piloto": "Perez", "equipe": "Red Bull Racing", "numero": 11, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2022, "circuito": "Marina Bay", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 2, "pontos": 18, "pole_position": "Sim"},

    # Etapa 18: Japão (Suzuka)
    {"ano": 2022, "circuito": "Suzuka", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2022, "circuito": "Suzuka", "piloto": "Perez", "equipe": "Red Bull Racing", "numero": 11, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 19: Estados Unidos (Austin)
    {"ano": 2022, "circuito": "Austin", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2022, "circuito": "Austin", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 20: Cidade do México (Hermanos Rodríguez)
    {"ano": 2022, "circuito": "Cidade do Mexico", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2022, "circuito": "Cidade do Mexico", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 21: São Paulo (Interlagos)
    {"ano": 2022, "circuito": "Interlagos", "piloto": "Russell", "equipe": "Mercedes", "numero": 63, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2022, "circuito": "Interlagos", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 22: Abu Dhabi (Yas Marina)
    {"ano": 2022, "circuito": "Yas Marina", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2022, "circuito": "Yas Marina", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 2, "pontos": 18, "pole_position": "Não"}

]

if __name__ == "__main__":
    print("Iniciando a carga de todas as temporadas históricas...")

# Soma as listas dos três anos
todas_as_corridas = corridas_2020 + corridas_2021 + corridas_2022

banco.salvar_no_banco(todas_as_corridas)
print("✅ Carga completa dos anos 2020, 2021 e 2022 realizada com sucesso!")

## TEMPORADA DE 2023

# --- TEMPORADA 2023 ---
corridas_2023 = [
    # Etapa 1: Bahrein (Sakhir)
    {"ano": 2023, "circuito": "Sakhir", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2023, "circuito": "Sakhir", "piloto": "Perez", "equipe": "Red Bull Racing", "numero": 11, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 2: Arábia Saudita (Jidá)
    {"ano": 2023, "circuito": "Jida", "piloto": "Perez", "equipe": "Red Bull Racing", "numero": 11, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2023, "circuito": "Jida", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 3: Austrália (Melbourne)
    {"ano": 2023, "circuito": "Albert Park", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2023, "circuito": "Albert Park", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 4: Azerbaijão (Baku)
    {"ano": 2023, "circuito": "Baku", "piloto": "Perez", "equipe": "Red Bull Racing", "numero": 11, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2023, "circuito": "Baku", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 5: Miami
    {"ano": 2023, "circuito": "Miami", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2023, "circuito": "Miami", "piloto": "Perez", "equipe": "Red Bull Racing", "numero": 11, "posicao": 2, "pontos": 18, "pole_position": "Sim"},

    # Etapa 6: Mônaco (Monte Carlo)
    {"ano": 2023, "circuito": "Monaco", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2023, "circuito": "Monaco", "piloto": "Alonso", "equipe": "Aston Martin", "numero": 14, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 7: Espanha (Barcelona)
    {"ano": 2023, "circuito": "Barcelona", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2023, "circuito": "Barcelona", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 8: Canadá (Montreal)
    {"ano": 2023, "circuito": "Montreal", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2023, "circuito": "Montreal", "piloto": "Alonso", "equipe": "Aston Martin", "numero": 14, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 9: Áustria (Spielberg)
    {"ano": 2023, "circuito": "Spielberg", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2023, "circuito": "Spielberg", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 10: Grã-Bretanha (Silverstone)
    {"ano": 2023, "circuito": "Silverstone", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2023, "circuito": "Silverstone", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 11: Hungria (Hungaroring)
    {"ano": 2023, "circuito": "Hungaroring", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2023, "circuito": "Hungaroring", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 12: Bélgica (Spa-Francorchamps)
    {"ano": 2023, "circuito": "Spa-Francorchamps", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2023, "circuito": "Spa-Francorchamps", "piloto": "Perez", "equipe": "Red Bull Racing", "numero": 11, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 13: Holanda (Zandvoort)
    {"ano": 2023, "circuito": "Zandvoort", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2023, "circuito": "Zandvoort", "piloto": "Alonso", "equipe": "Aston Martin", "numero": 14, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 14: Itália (Monza)
    {"ano": 2023, "circuito": "Monza", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2023, "circuito": "Monza", "piloto": "Perez", "equipe": "Red Bull Racing", "numero": 11, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 15: Singapura (Marina Bay)
    {"ano": 2023, "circuito": "Marina Bay", "piloto": "Sainz", "equipe": "Ferrari", "numero": 55, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2023, "circuito": "Marina Bay", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 16: Japão (Suzuka)
    {"ano": 2023, "circuito": "Suzuka", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2023, "circuito": "Suzuka", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 17: Catar (Losail)
    {"ano": 2023, "circuito": "Losail", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2023, "circuito": "Losail", "piloto": "Piastri", "equipe": "McLaren", "numero": 81, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 18: Estados Unidos (Austin)
    {"ano": 2023, "circuito": "Austin", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2023, "circuito": "Austin", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 19: Cidade do México (Hermanos Rodríguez)
    {"ano": 2023, "circuito": "Cidade do Mexico", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2023, "circuito": "Cidade do Mexico", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 20: São Paulo (Interlagos)
    {"ano": 2023, "circuito": "Interlagos", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2023, "circuito": "Interlagos", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 21: Las Vegas
    {"ano": 2023, "circuito": "Las Vegas", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2023, "circuito": "Las Vegas", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 2, "pontos": 18, "pole_position": "Sim"},

    # Etapa 22: Abu Dhabi (Yas Marina)
    {"ano": 2023, "circuito": "Yas Marina", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2023, "circuito": "Yas Marina", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 2, "pontos": 18, "pole_position": "Não"}
]

if __name__ == "__main__":
    print("Iniciando a carga de todas as temporadas históricas...")

    # Soma as listas de 2020 até 2023
    todas_as_corridas = corridas_2020 + corridas_2021 + corridas_2022 + corridas_2023

    banco.salvar_no_banco(todas_as_corridas)
    print("✅ Carga completa das temporadas 2020 a 2023 realizada com sucesso!")

## TEMPORADA DE 2024

# --- TEMPORADA 2024 ---
corridas_2024 = [
    # Etapa 1: Bahrein (Sakhir)
    {"ano": 2024, "circuito": "Sakhir", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2024, "circuito": "Sakhir", "piloto": "Perez", "equipe": "Red Bull Racing", "numero": 11, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 2: Arábia Saudita (Jidá)
    {"ano": 2024, "circuito": "Jida", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2024, "circuito": "Jida", "piloto": "Perez", "equipe": "Red Bull Racing", "numero": 11, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 3: Austrália (Melbourne)
    {"ano": 2024, "circuito": "Albert Park", "piloto": "Sainz", "equipe": "Ferrari", "numero": 55, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2024, "circuito": "Albert Park", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 4: Japão (Suzuka)
    {"ano": 2024, "circuito": "Suzuka", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2024, "circuito": "Suzuka", "piloto": "Perez", "equipe": "Red Bull Racing", "numero": 11, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 5: China (Xangai)
    {"ano": 2024, "circuito": "Xangai", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2024, "circuito": "Xangai", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 6: Miami
    {"ano": 2024, "circuito": "Miami", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2024, "circuito": "Miami", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 2, "pontos": 18, "pole_position": "Sim"},

    # Etapa 7: Emília-Romanha (Imola)
    {"ano": 2024, "circuito": "Imola", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2024, "circuito": "Imola", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 8: Mônaco (Monte Carlo)
    {"ano": 2024, "circuito": "Monaco", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2024, "circuito": "Monaco", "piloto": "Piastri", "equipe": "McLaren", "numero": 81, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 9: Canadá (Montreal)
    {"ano": 2024, "circuito": "Montreal", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2024, "circuito": "Montreal", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 10: Espanha (Barcelona)
    {"ano": 2024, "circuito": "Barcelona", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2024, "circuito": "Barcelona", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Sim"},

    # Etapa 11: Áustria (Spielberg)
    {"ano": 2024, "circuito": "Spielberg", "piloto": "Russell", "equipe": "Mercedes", "numero": 63, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2024, "circuito": "Spielberg", "piloto": "Piastri", "equipe": "McLaren", "numero": 81, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 12: Grã-Bretanha (Silverstone)
    {"ano": 2024, "circuito": "Silverstone", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2024, "circuito": "Silverstone", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 13: Hungria (Hungaroring)
    {"ano": 2024, "circuito": "Hungaroring", "piloto": "Piastri", "equipe": "McLaren", "numero": 81, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2024, "circuito": "Hungaroring", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Sim"},

    # Etapa 14: Bélgica (Spa-Francorchamps)
    {"ano": 2024, "circuito": "Spa-Francorchamps", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2024, "circuito": "Spa-Francorchamps", "piloto": "Piastri", "equipe": "McLaren", "numero": 81, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 15: Holanda (Zandvoort)
    {"ano": 2024, "circuito": "Zandvoort", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2024, "circuito": "Zandvoort", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 16: Itália (Monza)
    {"ano": 2024, "circuito": "Monza", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2024, "circuito": "Monza", "piloto": "Piastri", "equipe": "McLaren", "numero": 81, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 17: Azerbaijão (Baku)
    {"ano": 2024, "circuito": "Baku", "piloto": "Piastri", "equipe": "McLaren", "numero": 81, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2024, "circuito": "Baku", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 2, "pontos": 18, "pole_position": "Sim"},

    # Etapa 18: Singapura (Marina Bay)
    {"ano": 2024, "circuito": "Marina Bay", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2024, "circuito": "Marina Bay", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 19: Estados Unidos (Austin)
    {"ano": 2024, "circuito": "Austin", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2024, "circuito": "Austin", "piloto": "Sainz", "equipe": "Ferrari", "numero": 55, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 20: Cidade do México (Hermanos Rodríguez)
    {"ano": 2024, "circuito": "Cidade do Mexico", "piloto": "Sainz", "equipe": "Ferrari", "numero": 55, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2024, "circuito": "Cidade do Mexico", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 21: São Paulo (Interlagos)
    {"ano": 2024, "circuito": "Interlagos", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2024, "circuito": "Interlagos", "piloto": "Ocon", "equipe": "Alpine", "numero": 31, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 22: Las Vegas
    {"ano": 2024, "circuito": "Las Vegas", "piloto": "Russell", "equipe": "Mercedes", "numero": 63, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2024, "circuito": "Las Vegas", "piloto": "Hamilton", "equipe": "Mercedes", "numero": 44, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 23: Catar (Losail)
    {"ano": 2024, "circuito": "Losail", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2024, "circuito": "Losail", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 24: Abu Dhabi (Yas Marina)
    {"ano": 2024, "circuito": "Yas Marina", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2024, "circuito": "Yas Marina", "piloto": "Sainz", "equipe": "Ferrari", "numero": 55, "posicao": 2, "pontos": 18, "pole_position": "Não"}
]

if __name__ == "__main__":
    print("Iniciando a carga de todas as temporadas históricas...")

    # Soma as listas de 2020 até 2024
    todas_as_corridas = corridas_2020 + corridas_2021 + corridas_2022 + corridas_2023 + corridas_2024

    banco.salvar_no_banco(todas_as_corridas)
    print("✅ Carga completa das temporadas 2020 a 2024 realizada com sucesso!")

## TEMPORADA DE 2025

# --- TEMPORADA 2025 ---
corridas_2025 = [
    # Etapa 1: Austrália (Melbourne)
    {"ano": 2025, "circuito": "Albert Park", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2025, "circuito": "Albert Park", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 2: China (Xangai)
    {"ano": 2025, "circuito": "Xangai", "piloto": "Piastri", "equipe": "McLaren", "numero": 81, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2025, "circuito": "Xangai", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 3: Japão (Suzuka)
    {"ano": 2025, "circuito": "Suzuka", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2025, "circuito": "Suzuka", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 4: Bahrein (Sakhir)
    {"ano": 2025, "circuito": "Sakhir", "piloto": "Piastri", "equipe": "McLaren", "numero": 81, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2025, "circuito": "Sakhir", "piloto": "Russell", "equipe": "Mercedes", "numero": 63, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 5: Arábia Saudita (Jidá)
    {"ano": 2025, "circuito": "Jida", "piloto": "Piastri", "equipe": "McLaren", "numero": 81, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2025, "circuito": "Jida", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 2, "pontos": 18, "pole_position": "Sim"},

    # Etapa 6: Miami
    {"ano": 2025, "circuito": "Miami", "piloto": "Piastri", "equipe": "McLaren", "numero": 81, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2025, "circuito": "Miami", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 7: Emília-Romanha (Imola)
    {"ano": 2025, "circuito": "Imola", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2025, "circuito": "Imola", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 8: Mônaco (Monte Carlo)
    {"ano": 2025, "circuito": "Monaco", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2025, "circuito": "Monaco", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 9: Espanha (Barcelona)
    {"ano": 2025, "circuito": "Barcelona", "piloto": "Piastri", "equipe": "McLaren", "numero": 81, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2025, "circuito": "Barcelona", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 10: Canadá (Montreal)
    {"ano": 2025, "circuito": "Montreal", "piloto": "Russell", "equipe": "Mercedes", "numero": 63, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2025, "circuito": "Montreal", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 11: Áustria (Spielberg)
    {"ano": 2025, "circuito": "Spielberg", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2025, "circuito": "Spielberg", "piloto": "Piastri", "equipe": "McLaren", "numero": 81, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 12: Grã-Bretanha (Silverstone)
    {"ano": 2025, "circuito": "Silverstone", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2025, "circuito": "Silverstone", "piloto": "Piastri", "equipe": "McLaren", "numero": 81, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 13: Bélgica (Spa-Francorchamps)
    {"ano": 2025, "circuito": "Spa-Francorchamps", "piloto": "Piastri", "equipe": "McLaren", "numero": 81, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2025, "circuito": "Spa-Francorchamps", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Sim"},

    # Etapa 14: Hungria (Hungaroring)
    {"ano": 2025, "circuito": "Hungaroring", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2025, "circuito": "Hungaroring", "piloto": "Piastri", "equipe": "McLaren", "numero": 81, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 15: Holanda (Zandvoort)
    {"ano": 2025, "circuito": "Zandvoort", "piloto": "Piastri", "equipe": "McLaren", "numero": 81, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2025, "circuito": "Zandvoort", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 16: Itália (Monza)
    {"ano": 2025, "circuito": "Monza", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2025, "circuito": "Monza", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 17: Azerbaijão (Baku)
    {"ano": 2025, "circuito": "Baku", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2025, "circuito": "Baku", "piloto": "Russell", "equipe": "Mercedes", "numero": 63, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 18: Singapura (Marina Bay)
    {"ano": 2025, "circuito": "Marina Bay", "piloto": "Russell", "equipe": "Mercedes", "numero": 63, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2025, "circuito": "Marina Bay", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 19: Estados Unidos (Austin)
    {"ano": 2025, "circuito": "Austin", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2025, "circuito": "Austin", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 20: Cidade do México (Hermanos Rodríguez)
    {"ano": 2025, "circuito": "Cidade do Mexico", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2025, "circuito": "Cidade do Mexico", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 21: São Paulo (Interlagos)
    {"ano": 2025, "circuito": "Interlagos", "piloto": "Norris", "equipe": "McLaren", "numero": 4, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2025, "circuito": "Interlagos", "piloto": "Antonelli", "equipe": "Mercedes", "numero": 12, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 22: Las Vegas
    {"ano": 2025, "circuito": "Las Vegas", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2025, "circuito": "Las Vegas", "piloto": "Russell", "equipe": "Mercedes", "numero": 63, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 23: Catar (Losail)
    {"ano": 2025, "circuito": "Losail", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2025, "circuito": "Losail", "piloto": "Piastri", "equipe": "McLaren", "numero": 81, "posicao": 2, "pontos": 18, "pole_position": "Sim"},

    # Etapa 24: Abu Dhabi (Yas Marina)
    {"ano": 2025, "circuito": "Yas Marina", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2025, "circuito": "Yas Marina", "piloto": "Piastri", "equipe": "McLaren", "numero": 81, "posicao": 2, "pontos": 18, "pole_position": "Não"}
]

if __name__ == "__main__":
    print("Iniciando a carga de todas as temporadas históricas (2020-2025)...")

    # Unificação de todas as temporadas
    todas_as_corridas = (
            corridas_2020 +
            corridas_2021 +
            corridas_2022 +
            corridas_2023 +
            corridas_2024 +
            corridas_2025
    )

    banco.salvar_no_banco(todas_as_corridas)
    print("✅ Carga histórica completa realizada com sucesso!")
    print(
        "O seu banco de dados SQLite agora possui todo o histórico de 2020 a 2025 e está pronto para receber as corridas de 2026 via menu!")


##Temporada de 2026 ----- até agora
# --- TEMPORADA 2026 (ETAPAS REALIZADAS) ---
corridas_2026 = [
    # Etapa 1: Austrália (Albert Park)
    {"ano": 2026, "circuito": "Albert Park", "piloto": "Russell", "equipe": "Mercedes", "numero": 63, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2026, "circuito": "Albert Park", "piloto": "Antonelli", "equipe": "Mercedes", "numero": 12, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 2: China (Xangai)
    {"ano": 2026, "circuito": "Xangai", "piloto": "Antonelli", "equipe": "Mercedes", "numero": 12, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2026, "circuito": "Xangai", "piloto": "Russell", "equipe": "Mercedes", "numero": 63, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 3: Japão (Suzuka)
    {"ano": 2026, "circuito": "Suzuka", "piloto": "Antonelli", "equipe": "Mercedes", "numero": 12, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2026, "circuito": "Suzuka", "piloto": "Piastri", "equipe": "McLaren", "numero": 81, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 4: Miami
    {"ano": 2026, "circuito": "Miami", "piloto": "Antonelli", "equipe": "Mercedes", "numero": 12, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2026, "circuito": "Miami", "piloto": "Norris", "equipe": "McLaren", "numero": 1, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 5: Canadá (Montreal)
    {"ano": 2026, "circuito": "Montreal", "piloto": "Antonelli", "equipe": "Mercedes", "numero": 12, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2026, "circuito": "Montreal", "piloto": "Hamilton", "equipe": "Ferrari", "numero": 44, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 6: Mônaco (Monte Carlo)
    {"ano": 2026, "circuito": "Monaco", "piloto": "Antonelli", "equipe": "Mercedes", "numero": 12, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2026, "circuito": "Monaco", "piloto": "Hamilton", "equipe": "Ferrari", "numero": 44, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 7: Barcelona-Catalunha
    {"ano": 2026, "circuito": "Barcelona", "piloto": "Hamilton", "equipe": "Ferrari", "numero": 44, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2026, "circuito": "Barcelona", "piloto": "Russell", "equipe": "Mercedes", "numero": 63, "posicao": 2, "pontos": 18, "pole_position": "Sim"},

    # Etapa 8: Áustria (Spielberg)
    {"ano": 2026, "circuito": "Spielberg", "piloto": "Russell", "equipe": "Mercedes", "numero": 63, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2026, "circuito": "Spielberg", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 3, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 9: Grã-Bretanha (Silverstone)
    {"ano": 2026, "circuito": "Silverstone", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2026, "circuito": "Silverstone", "piloto": "Russell", "equipe": "Mercedes", "numero": 63, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 10: Bélgica (Spa-Francorchamps)
    {"ano": 2026, "circuito": "Spa-Francorchamps", "piloto": "Antonelli", "equipe": "Mercedes", "numero": 12, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2026, "circuito": "Spa-Francorchamps", "piloto": "Leclerc", "equipe": "Ferrari", "numero": 16, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 11: Hungria (Hungaroring)
    {"ano": 2026, "circuito": "Hungaroring", "piloto": "Norris", "equipe": "McLaren", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2026, "circuito": "Hungaroring", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 3, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 12: Países Baixos (Zandvoort)
    {"ano": 2026, "circuito": "Zandvoort", "piloto": "Norris", "equipe": "McLaren", "numero": 1, "posicao": 1, "pontos": 25, "pole_position": "Sim"},
    {"ano": 2026, "circuito": "Zandvoort", "piloto": "Antonelli", "equipe": "Mercedes", "numero": 12, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 13: Itália (Monza)
    {"ano": 2026, "circuito": "Monza", "piloto": "Antonelli", "equipe": "Mercedes", "numero": 12, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2026, "circuito": "Monza", "piloto": "Russell", "equipe": "Mercedes", "numero": 63, "posicao": 2, "pontos": 18, "pole_position": "Não"},

    # Etapa 14: Espanha (Madri)
    {"ano": 2026, "circuito": "Madri", "piloto": "Antonelli", "equipe": "Mercedes", "numero": 12, "posicao": 1, "pontos": 25, "pole_position": "Não"},
    {"ano": 2026, "circuito": "Madri", "piloto": "Verstappen", "equipe": "Red Bull Racing", "numero": 3, "posicao": 2, "pontos": 18, "pole_position": "Não"}
]
if __name__ == "__main__":
    print("Iniciando a carga de todas as temporadas (2020-2026)...")

    todas_as_corridas = (
            corridas_2020 +
            corridas_2021 +
            corridas_2022 +
            corridas_2023 +
            corridas_2024 +
            corridas_2025 +
            corridas_2026
    )

    banco.salvar_no_banco(todas_as_corridas)
    print("✅ Carga completa realizada com sucesso!")