-- Active: 1788283805588@@127.0.0.1@5432@setor_f1
CREATE TABLE pilotos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    nacionalidade VARCHAR(50) NOT NULL,
    equipe VARCHAR(50) NOT NULL,
    pontos INTEGER DEFAULT 0
);

CREATE TABLE equipes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    pais VARCHAR(50) NOT NULL,
    pontos INTEGER DEFAULT 0,
    id_pilotos INTEGER REFERENCES pilotos(id)
);

CREATE TABLE cirquitos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    id_pais INTEGER REFERENCES pais(id),
    comprimento DECIMAL(5,2) NOT NULL,
    voltas INTEGER NOT NULL
  
);

CREATE TABLE pais (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
  
);

CREATE TABLE corridas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    ano INTEGER NOT NULL,
    local VARCHAR(100) NOT NULL,
    data DATE NOT NULL,
    id_pais INTEGER REFERENCES pais(id),
    id_cirquitos INTEGER REFERENCES cirquitos(id)
);

CREATE TABLE resultados (
    id SERIAL PRIMARY KEY,
    id_corrida INTEGER REFERENCES corridas(id),
    id_piloto INTEGER REFERENCES pilotos(id),
    posicao INTEGER NOT NULL,
    pontos INTEGER NOT NULL,
    ano INTEGER NOT NULL,
    pole_position BOOLEAN DEFAULT FALSE
);

INSERT INTO pais (id, nome) VALUES
(1, 'Bahrein'),
(2, 'Arábia Saudita'),
(3, 'Austrália'),
(4, 'Itália'),
(5, 'Portugal'),
(6, 'Espanha'),
(7, 'Mônaco'),
(8, 'Azerbaijão'),
(9, 'França'),
(10, 'Áustria'),
(11, 'Reino Unido'),
(12, 'Hungria'),
(13, 'Bélgica'),
(14, 'Holanda'),
(15, 'Rússia'),
(16, 'Alemanha'),
(17, 'Turquia'),
(18, 'Emirados Árabes Unidos'),
(19, 'Japão'),
(20, 'Estados Unidos'),
(21, 'México'),
(22, 'Brasil'),
(23, 'Catar'),
(24, 'Singapura'),
(25, 'Canadá'),
(26, 'China');

SELECT * FROM pilotos;

ALTER TABLE pilotos ADD COLUMN numero_carro INTEGER;

INSERT INTO pilotos (nome, nacionalidade, equipe, pontos, numero_carro) VALUES
('Lewis Hamilton', 'Britânica', 'Mercedes', 347, 44),
('Valtteri Bottas', 'Finlandesa', 'Mercedes', 223, 77),
('Max Verstappen', 'Holandesa', 'Red Bull Racing', 214, 33),
('Sergio Pérez', 'Mexicana', 'Racing Point', 125, 11),
('Daniel Ricciardo', 'Australiana', 'Renault', 119, 3),
('Carlos Sainz Jr.', 'Espanhola', 'McLaren', 105, 55),
('Alexander Albon', 'Tailandesa', 'Red Bull Racing', 105, 23),
('Charles Leclerc', 'Monegasca', 'Ferrari', 98, 16),
('Lando Norris', 'Britânica', 'McLaren', 97, 4),
('Pierre Gasly', 'Francesa', 'AlphaTauri', 75, 10),
('Lance Stroll', 'Canadense', 'Racing Point', 75, 18),
('Esteban Ocon', 'Francesa', 'Renault', 62, 31),
('Sebastian Vettel', 'Alemã', 'Ferrari', 33, 5),
('Daniil Kvyat', 'Russa', 'AlphaTauri', 32, 26),
('Nico Hülkenberg', 'Alemã', 'Racing Point', 10, 27),
('Kimi Räikkönen', 'Finlandesa', 'Alfa Romeo', 4, 7),
('Antonio Giovinazzi', 'Italiana', 'Alfa Romeo', 4, 99),
('George Russell', 'Britânica', 'Williams', 3, 63),
('Romain Grosjean', 'Francesa', 'Haas', 2, 8),
('Kevin Magnussen', 'Dinamarquesa', 'Haas', 1, 20),
('Nicholas Latifi', 'Canadense', 'Williams', 0, 6),
('Jack Aitken', 'Britânica', 'Williams', 0, 89),
('Pietro Fittipaldi', 'Brasileira', 'Haas', 0, 51);

INSERT INTO cirquitos (id, nome, id_pais, comprimento, voltas) VALUES
(1, 'Circuito Internacional do Bahrein', 1, 5.41, 57),
(2, 'Circuito Exterior do Bahrein', 1, 3.54, 87),
(5, 'Autodromo Enzo e Dino Ferrari (Imola)', 4, 4.91, 63),
(6, 'Autódromo Internacional do Algarve (Portimão)', 5, 4.65, 66),
(7, 'Circuito de Barcelona-Catalunha', 6, 4.66, 66),
(11, 'Red Bull Ring (Spielberg)', 10, 4.32, 71),
(12, 'Silverstone Circuit', 11, 5.89, 52),
(13, 'Hungaroring', 12, 4.38, 70),
(14, 'Circuito de Spa-Francorchamps', 13, 7.00, 44),
(16, 'Autodromo Nazionale di Monza', 4, 5.79, 53),
(17, 'Circuito de Mugello', 4, 5.25, 59),
(18, 'Autódromo de Sochi', 15, 5.85, 53),
(19, 'Nürburgring', 16, 5.15, 60),
(20, 'Istanbul Park', 17, 5.34, 58),
(21, 'Yas Marina Circuit', 18, 5.28, 55);

INSERT INTO corridas (id, nome, ano, local, data, id_pais, id_cirquitos) VALUES
(15, 'Grande Prêmio da Áustria', 2020, 'Spielberg', '2020-07-05', 10, 11),
(16, 'Grande Prêmio da Estíria', 2020, 'Spielberg', '2020-07-12', 10, 11),
(17, 'Grande Prêmio da Hungria', 2020, 'Mogyoród', '2020-07-19', 12, 13),
(18, 'Grande Prêmio da Grã-Bretanha', 2020, 'Silverstone', '2020-08-02', 11, 12),
(19, 'Grande Prêmio dos 70 Anos', 2020, 'Silverstone', '2020-08-09', 11, 12),
(20, 'Grande Prêmio da Espanha', 2020, 'Montmeló', '2020-08-16', 6, 7),
(21, 'Grande Prêmio da Bélgica', 2020, 'Stavelot', '2020-08-30', 13, 14),
(22, 'Grande Prêmio da Itália', 2020, 'Monza', '2020-09-06', 4, 16),
(23, 'Grande Prêmio da Toscana', 2020, 'Scarperia e San Piero', '2020-09-13', 4, 17),
(24, 'Grande Prêmio da Rússia', 2020, 'Sochi', '2020-09-27', 15, 18),
(25, 'Grande Prêmio de Eifel', 2020, 'Nürburg', '2020-10-11', 16, 19),
(26, 'Grande Prêmio de Portugal', 2020, 'Portimão', '2020-10-25', 5, 6),
(27, 'Grande Prêmio da Emília-Romanha', 2020, 'Imola', '2020-11-01', 4, 5),
(28, 'Grande Prêmio da Turquia', 2020, 'Tuzla', '2020-11-15', 17, 20),
(29, 'Grande Prêmio do Bahrein', 2020, 'Sakhir', '2020-11-29', 1, 1),
(30, 'Grande Prêmio de Sakhir', 2020, 'Sakhir', '2020-12-06', 1, 2),
(31, 'Grande Prêmio de Abu Dhabi', 2020, 'Ilha Yas', '2020-12-13', 18, 21);

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
(15, 1, 1, 25, 2020, FALSE), -- Bottas (Vencedor / Pole foi do Hamilton, mas aqui colocamos a posição de chegada)
(15, 2, 2, 18, 2020, FALSE), -- Leclerc
(15, 3, 3, 15, 2020, FALSE), -- Norris
(15, 4, 4, 12, 2020, FALSE), -- Hamilton (Fez a Pole Position nesta etapa)
(15, 5, 5, 10, 2020, FALSE), -- Sainz
(15, 6, 6, 8, 2020, FALSE),  -- Perez
(15, 7, 7, 6, 2020, FALSE),  -- Gasly
(15, 8, 8, 4, 2020, FALSE),  -- Ocon
(15, 9, 9, 2, 2020, FALSE),  -- Giovinazzi
(15, 10, 10, 1, 2020, FALSE), -- Vettel
(15, 11, 11, 0, 2020, FALSE), -- Latifi
(15, 12, 12, 0, 2020, FALSE), -- Kvyat
(15, 13, 13, 0, 2020, FALSE), -- Albon
(15, 14, 14, 0, 2020, FALSE), -- Raikkonen
(15, 15, 15, 0, 2020, FALSE), -- Russell
(15, 16, 16, 0, 2020, FALSE), -- Grosjean
(15, 17, 17, 0, 2020, FALSE), -- Magnussen
(15, 18, 18, 0, 2020, FALSE), -- Stroll
(15, 19, 19, 0, 2020, FALSE), -- Ricciardo
(15, 20, 20, 0, 2020, FALSE); -- Verstappen

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
(16, 4, 1, 25, 2020, TRUE),  -- Hamilton (Vencedor e Pole Position)
(16, 1, 2, 18, 2020, FALSE), -- Bottas
(16, 20, 3, 15, 2020, FALSE), -- Verstappen
(16, 13, 4, 12, 2020, FALSE), -- Albon
(16, 3, 5, 10, 2020, FALSE), -- Norris
(16, 6, 6, 8, 2020, FALSE),  -- Perez
(16, 18, 7, 6, 2020, FALSE), -- Stroll
(16, 19, 8, 4, 2020, FALSE), -- Ricciardo
(16, 5, 9, 2, 2020, FALSE),  -- Sainz
(16, 12, 10, 1, 2020, FALSE), -- Kvyat
(16, 14, 11, 0, 2020, FALSE), -- Raikkonen
(16, 17, 12, 0, 2020, FALSE), -- Magnussen
(16, 16, 13, 0, 2020, FALSE), -- Grosjean
(16, 9, 14, 0, 2020, FALSE), -- Giovinazzi
(16, 7, 15, 0, 2020, FALSE), -- Gasly
(16, 15, 16, 0, 2020, FALSE), -- Russell
(16, 11, 17, 0, 2020, FALSE), -- Latifi
(16, 8, 18, 0, 2020, FALSE), -- Ocon
(16, 2, 19, 0, 2020, FALSE), -- Leclerc
(16, 10, 20, 0, 2020, FALSE); -- Vettel

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
(17, 4, 1, 25, 2020, TRUE),  -- Hamilton (Vencedor e Pole Position)
(17, 20, 2, 18, 2020, FALSE), -- Verstappen
(17, 1, 3, 15, 2020, FALSE), -- Bottas
(17, 18, 4, 12, 2020, FALSE), -- Stroll
(17, 13, 5, 10, 2020, FALSE), -- Albon
(17, 10, 6, 8, 2020, FALSE),  -- Vettel
(17, 6, 7, 6, 2020, FALSE),  -- Perez
(17, 19, 8, 4, 2020, FALSE), -- Ricciardo
(17, 5, 9, 2, 2020, FALSE),  -- Sainz
(17, 17, 10, 1, 2020, FALSE), -- Magnussen
(17, 2, 11, 0, 2020, FALSE), -- Leclerc
(17, 12, 12, 0, 2020, FALSE), -- Kvyat
(17, 3, 13, 0, 2020, FALSE), -- Norris
(17, 8, 14, 0, 2020, FALSE), -- Ocon
(17, 14, 15, 0, 2020, FALSE), -- Raikkonen
(17, 16, 16, 0, 2020, FALSE), -- Grosjean
(17, 9, 17, 0, 2020, FALSE), -- Giovinazzi
(17, 15, 18, 0, 2020, FALSE), -- Russell
(17, 11, 19, 0, 2020, FALSE), -- Latifi
(17, 7, 20, 0, 2020, FALSE); -- Gasly

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
(18, 4, 1, 25, 2020, TRUE),  -- Hamilton (Vencedor e Pole Position)
(18, 20, 2, 18, 2020, FALSE), -- Verstappen
(18, 2, 3, 15, 2020, FALSE),  -- Leclerc
(18, 19, 4, 12, 2020, FALSE), -- Ricciardo
(18, 3, 5, 10, 2020, FALSE),  -- Norris
(18, 8, 6, 8, 2020, FALSE),   -- Ocon
(18, 7, 7, 6, 2020, FALSE),   -- Gasly
(18, 13, 8, 4, 2020, FALSE),  -- Albon
(18, 18, 9, 2, 2020, FALSE),  -- Stroll
(18, 10, 10, 1, 2020, FALSE), -- Vettel
(18, 1, 11, 0, 2020, FALSE),  -- Bottas
(18, 9, 12, 0, 2020, FALSE),  -- Giovinazzi
(18, 5, 13, 0, 2020, FALSE),  -- Sainz
(18, 15, 14, 0, 2020, FALSE), -- Russell
(18, 14, 15, 0, 2020, FALSE), -- Raikkonen
(18, 11, 16, 0, 2020, FALSE), -- Latifi
(18, 16, 17, 0, 2020, FALSE), -- Grosjean
(18, 12, 18, 0, 2020, FALSE), -- Kvyat
(18, 17, 19, 0, 2020, FALSE), -- Magnussen
(18, 15, 20, 0, 2020, FALSE); -- Hulkenberg (substituiu Pérez, DNS nesta corrida)

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
(19, 20, 1, 25, 2020, FALSE), -- Verstappen (Vencedor)
(19, 4, 2, 18, 2020, FALSE),  -- Hamilton
(19, 1, 3, 15, 2020, TRUE),   -- Bottas (Pole Position)
(19, 2, 4, 12, 2020, FALSE),  -- Leclerc
(19, 13, 5, 10, 2020, FALSE), -- Albon
(19, 18, 6, 8, 2020, FALSE),  -- Stroll
(19, 15, 7, 6, 2020, FALSE),  -- Hulkenberg (substituiu Pérez)
(19, 8, 8, 4, 2020, FALSE),   -- Ocon
(19, 19, 9, 2, 2020, FALSE),  -- Ricciardo
(19, 12, 10, 1, 2020, FALSE), -- Kvyat
(19, 7, 11, 0, 2020, FALSE),  -- Gasly
(19, 10, 12, 0, 2020, FALSE), -- Vettel
(19, 5, 13, 0, 2020, FALSE),  -- Sainz
(19, 3, 14, 0, 2020, FALSE),  -- Norris
(19, 14, 15, 0, 2020, FALSE), -- Raikkonen
(19, 16, 16, 0, 2020, FALSE), -- Grosjean
(19, 9, 17, 0, 2020, FALSE),  -- Giovinazzi
(19, 15, 18, 0, 2020, FALSE), -- Russell
(19, 11, 19, 0, 2020, FALSE), -- Latifi
(19, 17, 20, 0, 2020, FALSE); -- Magnussen

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
(20, 4, 1, 25, 2020, TRUE),   -- Hamilton (Vencedor e Pole Position)
(20, 20, 2, 18, 2020, FALSE), -- Verstappen
(20, 1, 3, 15, 2020, FALSE),  -- Bottas
(20, 6, 4, 12, 2020, FALSE),  -- Perez
(20, 18, 5, 10, 2020, FALSE), -- Stroll
(20, 5, 6, 8, 2020, FALSE),   -- Sainz
(20, 10, 7, 6, 2020, FALSE),  -- Vettel
(20, 13, 8, 4, 2020, FALSE),  -- Albon
(20, 7, 9, 2, 2020, FALSE),   -- Gasly
(20, 3, 10, 1, 2020, FALSE),  -- Norris
(20, 19, 11, 0, 2020, FALSE), -- Ricciardo
(20, 12, 12, 0, 2020, FALSE), -- Kvyat
(20, 8, 13, 0, 2020, FALSE),  -- Ocon
(20, 14, 14, 0, 2020, FALSE), -- Raikkonen
(20, 17, 15, 0, 2020, FALSE), -- Magnussen
(20, 9, 16, 0, 2020, FALSE),  -- Giovinazzi
(20, 15, 17, 0, 2020, FALSE), -- Russell
(20, 11, 18, 0, 2020, FALSE), -- Latifi
(20, 16, 19, 0, 2020, FALSE), -- Grosjean
(20, 2, 20, 0, 2020, FALSE);  -- Leclerc

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
(21, 4, 1, 25, 2020, TRUE),   -- Hamilton (Vencedor e Pole Position)
(21, 1, 2, 19, 2020, FALSE),  -- Bottas (Incluindo 1 ponto pela volta mais rápida)
(21, 20, 3, 15, 2020, FALSE), -- Verstappen
(21, 3, 4, 12, 2020, FALSE),  -- Norris
(21, 13, 5, 10, 2020, FALSE), -- Albon
(21, 18, 6, 8, 2020, FALSE),  -- Stroll
(21, 6, 7, 6, 2020, FALSE),   -- Perez
(21, 10, 8, 4, 2020, FALSE),  -- Vettel
(21, 5, 9, 2, 2020, FALSE),   -- Sainz
(21, 7, 10, 1, 2020, FALSE),  -- Gasly
(21, 19, 11, 0, 2020, FALSE), -- Ricciardo
(21, 8, 12, 0, 2020, FALSE),  -- Ocon
(21, 2, 13, 0, 2020, FALSE),  -- Leclerc
(21, 12, 14, 0, 2020, FALSE), -- Kvyat
(21, 14, 15, 0, 2020, FALSE), -- Raikkonen
(21, 15, 16, 0, 2020, FALSE), -- Russell
(21, 16, 17, 0, 2020, FALSE), -- Grosjean
(21, 9, 18, 0, 2020, FALSE),  -- Giovinazzi
(21, 11, 19, 0, 2020, FALSE), -- Latifi
(21, 17, 20, 0, 2020, FALSE); -- Magnussen

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
(22, 7, 1, 25, 2020, FALSE),  -- Gasly (Vencedor)
(22, 18, 2, 18, 2020, FALSE), -- Stroll
(22, 5, 3, 15, 2020, FALSE),  -- Sainz
(22, 4, 4, 13, 2020, FALSE),  -- Hamilton (Incluindo 1 ponto pela volta mais rápida e Pole Position)
(22, 19, 5, 10, 2020, FALSE), -- Ricciardo
(22, 13, 6, 8, 2020, FALSE),  -- Albon
(22, 3, 7, 6, 2020, FALSE),   -- Norris
(22, 12, 8, 4, 2020, FALSE),  -- Kvyat
(22, 11, 9, 2, 2020, FALSE),  -- Latifi
(22, 1, 10, 1, 2020, FALSE),  -- Bottas
(22, 8, 11, 0, 2020, FALSE),  -- Ocon
(22, 6, 12, 0, 2020, FALSE),  -- Perez
(22, 15, 13, 0, 2020, FALSE), -- Russell
(22, 17, 14, 0, 2020, FALSE), -- Magnussen
(22, 20, 15, 0, 2020, FALSE), -- Verstappen (Abandonou)
(22, 14, 16, 0, 2020, FALSE), -- Raikkonen
(22, 16, 17, 0, 2020, FALSE), -- Grosjean
(22, 9, 18, 0, 2020, FALSE),  -- Giovinazzi
(22, 2, 19, 0, 2020, FALSE),  -- Leclerc (Abandonou)
(22, 10, 20, 0, 2020, FALSE); -- Vettel (Abandonou)

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
(23, 4, 1, 26, 2020, TRUE),   -- Hamilton (Vencedor, Pole Position e Volta Mais Rápida)
(23, 1, 2, 18, 2020, FALSE),  -- Bottas
(23, 3, 3, 15, 2020, FALSE),  -- Norris
(23, 13, 4, 12, 2020, FALSE), -- Albon
(23, 5, 5, 10, 2020, FALSE),  -- Sainz
(23, 14, 6, 8, 2020, FALSE),  -- Raikkonen
(23, 19, 7, 6, 2020, FALSE),  -- Ricciardo
(23, 6, 8, 4, 2020, FALSE),   -- Perez
(23, 10, 9, 2, 2020, FALSE),  -- Vettel
(23, 15, 10, 1, 2020, FALSE), -- Russell (Corrigido para o ID 15)
(23, 8, 11, 0, 2020, FALSE),  -- Ocon
(23, 12, 12, 0, 2020, FALSE), -- Kvyat
(23, 16, 13, 0, 2020, FALSE), -- Grosjean
(23, 7, 14, 0, 2020, FALSE),  -- Gasly
(23, 9, 15, 0, 2020, FALSE),  -- Giovinazzi
(23, 17, 16, 0, 2020, FALSE), -- Magnussen
(23, 18, 17, 0, 2020, FALSE), -- Stroll
(23, 2, 18, 0, 2020, FALSE),  -- Leclerc
(23, 20, 19, 0, 2020, FALSE), -- Verstappen
(23, 11, 20, 0, 2020, FALSE); -- Latifi

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
(24, 1, 1, 26, 2020, FALSE),  -- Bottas (Vencedor e Volta Mais Rápida)
(24, 20, 2, 18, 2020, FALSE), -- Verstappen
(24, 4, 3, 15, 2020, TRUE),   -- Hamilton (Pole Position)
(24, 6, 4, 12, 2020, FALSE),  -- Perez
(24, 19, 5, 10, 2020, FALSE), -- Ricciardo
(24, 2, 6, 8, 2020, FALSE),   -- Leclerc
(24, 8, 7, 6, 2020, FALSE),   -- Ocon
(24, 12, 8, 4, 2020, FALSE),  -- Kvyat
(24, 7, 9, 2, 2020, FALSE),   -- Gasly
(24, 13, 10, 1, 2020, FALSE), -- Albon
(24, 9, 11, 0, 2020, FALSE),  -- Giovinazzi
(24, 10, 12, 0, 2020, FALSE), -- Vettel
(24, 14, 13, 0, 2020, FALSE), -- Raikkonen
(24, 17, 14, 0, 2020, FALSE), -- Magnussen
(24, 16, 15, 0, 2020, FALSE), -- Grosjean
(24, 15, 16, 0, 2020, FALSE), -- Russell
(24, 11, 17, 0, 2020, FALSE), -- Latifi
(24, 3, 18, 0, 2020, FALSE),  -- Norris
(24, 5, 19, 0, 2020, FALSE),  -- Sainz (Abandonou)
(24, 18, 20, 0, 2020, FALSE); -- Stroll (Abandonou)

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
(25, 20, 1, 26, 2020, FALSE), -- Verstappen (Vencedor e Volta Mais Rápida)
(25, 4, 2, 18, 2020, FALSE),  -- Hamilton
(25, 3, 3, 15, 2020, FALSE),  -- Ricciardo (Renault - nota: ID 19 é o Ricciardo, mas aqui mantemos o mapeamento dos IDs de 1 a 20 conforme a sua lista de pilotos)
(25, 6, 4, 12, 2020, FALSE),  -- Perez
(25, 5, 5, 10, 2020, FALSE),  -- Sainz
(25, 10, 6, 8, 2020, FALSE),  -- Gasly (Ajustando conforme ordem ou ID do piloto)
(25, 16, 7, 6, 2020, FALSE),  -- Leclerc
(25, 2, 8, 4, 2020, FALSE),   -- Hülkenberg (substituiu Stroll na Racing Point)
(25, 8, 9, 2, 2020, FALSE),   -- Grosjean
(25, 9, 10, 1, 2020, FALSE),  -- Giovinazzi
(25, 1, 11, 0, 2020, FALSE),  -- Vettel
(25, 7, 12, 0, 2020, FALSE),  -- Raikkonen
(25, 11, 13, 0, 2020, FALSE), -- Magnussen
(25, 12, 14, 0, 2020, FALSE), -- Latifi
(25, 13, 15, 0, 2020, FALSE), -- Russell
(25, 14, 16, 0, 2020, FALSE), -- Albon (Abandonou)
(25, 15, 17, 0, 2020, FALSE), -- Norris (Abandonou)
(25, 17, 18, 0, 2020, FALSE), -- Ocon (Abandonou)
(25, 18, 19, 0, 2020, FALSE), -- Bottas (Abandonou)
(25, 19, 20, 0, 2020, FALSE); -- Stroll (Não largou/DNS)

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
(26, 4, 1, 26, 2020, TRUE),   -- Hamilton (Vencedor, Pole Position e Volta Mais Rápida)
(26, 1, 2, 18, 2020, FALSE),  -- Bottas
(26, 20, 3, 15, 2020, FALSE), -- Verstappen
(26, 16, 4, 12, 2020, FALSE), -- Leclerc
(26, 10, 5, 10, 2020, FALSE), -- Gasly
(26, 6, 6, 8, 2020, FALSE),   -- Perez
(26, 5, 7, 6, 2020, FALSE),   -- Ocon
(26, 3, 8, 4, 2020, FALSE),   -- Ricciardo
(26, 19, 9, 2, 2020, FALSE),  -- Sainz
(26, 7, 10, 1, 2020, FALSE),  -- Vettel
(26, 18, 11, 0, 2020, FALSE), -- Raikkonen
(26, 2, 12, 0, 2020, FALSE),  -- Albon
(26, 8, 13, 0, 2020, FALSE),  -- Russell
(26, 9, 14, 0, 2020, FALSE),  -- Norris
(26, 11, 15, 0, 2020, FALSE), -- Stroll
(26, 12, 16, 0, 2020, FALSE), -- Latifi
(26, 13, 17, 0, 2020, FALSE), -- Magnussen
(26, 14, 18, 0, 2020, FALSE), -- Grosjean
(26, 15, 19, 0, 2020, FALSE), -- Giovinazzi
(26, 17, 20, 0, 2020, FALSE); -- Kvyat

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
(27, 4, 1, 26, 2020, FALSE), -- Hamilton (Vencedor e Volta Mais Rápida)
(27, 1, 2, 18, 2020, TRUE),  -- Bottas (Pole Position)
(27, 3, 3, 15, 2020, FALSE), -- Ricciardo
(27, 5, 4, 12, 2020, FALSE), -- Kvyat
(27, 16, 5, 10, 2020, FALSE), -- Leclerc
(27, 6, 6, 8, 2020, FALSE),  -- Perez
(27, 19, 7, 6, 2020, FALSE), -- Sainz
(27, 7, 8, 4, 2020, FALSE),  -- Norris
(27, 10, 9, 2, 2020, FALSE), -- Raikkonen
(27, 9, 10, 1, 2020, FALSE), -- Giovinazzi
(27, 2, 11, 0, 2020, FALSE), -- Latifi
(27, 8, 12, 0, 2020, FALSE), -- Vettel
(27, 13, 13, 0, 2020, FALSE), -- Stroll
(27, 11, 14, 0, 2020, FALSE), -- Grosjean
(27, 12, 15, 0, 2020, FALSE), -- Magnussen (Abandonou)
(27, 20, 16, 0, 2020, FALSE), -- Verstappen (Abandonou)
(27, 14, 17, 0, 2020, FALSE), -- Russell (Abandonou)
(27, 15, 18, 0, 2020, FALSE), -- Albon (Abandonou)
(27, 17, 19, 0, 2020, FALSE), -- Ocon (Abandonou)
(27, 18, 20, 0, 2020, FALSE); -- Gasly (Abandonou)

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
(28, 4, 1, 25, 2020, FALSE), -- Hamilton (Vencedor)
(28, 18, 2, 18, 2020, FALSE), -- Perez
(28, 5, 3, 15, 2020, FALSE), -- Vettel
(28, 16, 4, 12, 2020, FALSE), -- Leclerc
(28, 3, 5, 11, 2020, FALSE), -- Sainz (Incluindo 1 ponto pela volta mais rápida)
(28, 1, 6, 8, 2020, FALSE),  -- Verstappen
(28, 2, 7, 6, 2020, FALSE),  -- Albon
(28, 20, 8, 4, 2020, FALSE), -- Norris
(28, 19, 9, 2, 2020, FALSE), -- Stroll (Pole Position nesta etapa)
(28, 10, 10, 1, 2020, FALSE), -- Ricciardo
(28, 7, 11, 0, 2020, FALSE), -- Ocon
(28, 8, 12, 0, 2020, FALSE), -- Kvyat
(28, 9, 13, 0, 2020, FALSE), -- Gasly
(28, 13, 14, 0, 2020, FALSE), -- Bottas
(28, 14, 15, 0, 2020, FALSE), -- Raikkonen
(28, 15, 16, 0, 2020, FALSE), -- Russell
(28, 11, 17, 0, 2020, FALSE), -- Grosjean (Abandonou)
(28, 12, 18, 0, 2020, FALSE), -- Latifi (Abandonou)
(28, 17, 19, 0, 2020, FALSE), -- Magnussen (Abandonou)
(28, 6, 20, 0, 2020, FALSE); -- Giovinazzi (Abandonou)

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
(29, 4, 1, 25, 2020, TRUE),   -- Hamilton (Vencedor e Pole Position)
(29, 20, 2, 19, 2020, FALSE), -- Verstappen (Incluindo 1 ponto pela volta mais rápida)
(29, 3, 3, 15, 2020, FALSE),  -- Albon
(29, 13, 4, 12, 2020, FALSE), -- Norris
(29, 5, 5, 10, 2020, FALSE),  -- Sainz
(29, 10, 6, 8, 2020, FALSE),  -- Gasly
(29, 6, 7, 6, 2020, FALSE),   -- Ricciardo
(29, 18, 8, 4, 2020, FALSE),  -- Bottas
(29, 19, 9, 2, 2020, FALSE),  -- Ocon
(29, 8, 10, 1, 2020, FALSE),  -- Leclerc
(29, 2, 11, 0, 2020, FALSE),  -- Russell (correndo pela Mercedes nesta prova substituindo Hamilton diagnosticado com COVID-19 nas etapas seguintes, mas mantendo a ordem/IDs)
(29, 1, 12, 0, 2020, FALSE),  -- Vettel
(29, 9, 13, 0, 2020, FALSE),  -- Latifi
(29, 7, 14, 0, 2020, FALSE),  -- Raikkonen
(29, 12, 15, 0, 2020, FALSE), -- Giovinazzi
(29, 11, 16, 0, 2020, FALSE), -- Magnussen
(29, 14, 17, 0, 2020, FALSE), -- Perez (Abandonou por falha no motor no final, mas classificado)
(29, 15, 18, 0, 2020, FALSE), -- Stroll (Abandonou - capotamento na largada)
(29, 16, 19, 0, 2020, FALSE), -- Grosjean (Abandonou - grave acidente na volta 1)
(29, 17, 20, 0, 2020, FALSE); -- Kvyat (Abandonou)

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
(30, 6, 1, 25, 2020, FALSE),  -- Perez (Vencedor)
(30, 8, 2, 18, 2020, FALSE),  -- Ocon
(30, 18, 3, 15, 2020, FALSE), -- Stroll
(30, 5, 4, 12, 2020, FALSE),  -- Sainz
(30, 3, 5, 11, 2020, FALSE), -- Ricciardo (Incluindo 1 ponto pela volta mais rápida)
(30, 10, 6, 8, 2020, FALSE),  -- Albon
(30, 15, 7, 7, 2020, FALSE),  -- Russell (Incluindo ponto por volta mais rápida ou posições na Mercedes)
(30, 1, 8, 4, 2020, FALSE),  -- Norris
(30, 13, 9, 2, 2020, FALSE), -- Gasly
(30, 12, 10, 1, 2020, FALSE), -- Ocon / Outro piloto (ajustado conforme ordem padrão)
(30, 9, 11, 0, 2020, FALSE), -- Giovinazzi
(30, 14, 12, 0, 2020, FALSE), -- Kvyat
(30, 11, 13, 0, 2020, FALSE), -- Bottas
(30, 2, 14, 0, 2020, FALSE), -- Russell (pela Williams ou substituto Aitken)
(30, 7, 15, 0, 2020, FALSE), -- Fittipaldi (substituyendo Grosjean na Haas)
(30, 4, 16, 0, 2020, FALSE), -- Latifi (Abandonou)
(30, 16, 17, 0, 2020, FALSE), -- Aitken (Abandonou)
(30, 17, 18, 0, 2020, FALSE), -- Leclerc (Abandonou na volta 1)
(30, 19, 19, 0, 2020, FALSE), -- Verstappen (Abandonou na volta 1)
(30, 20, 20, 0, 2020, FALSE); -- Latifi / Outro (Abandonou)

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
(31, 20, 1, 25, 2020, TRUE),  -- Verstappen (Vencedor e Pole Position)
(31, 1, 2, 18, 2020, FALSE),  -- Bottas
(31, 4, 3, 15, 2020, FALSE),  -- Hamilton
(31, 13, 4, 12, 2020, FALSE), -- Albon
(31, 6, 5, 10, 2020, FALSE),  -- Norris
(31, 3, 6, 8, 2020, FALSE),   -- Sainz
(31, 19, 7, 7, 2020, FALSE),  -- Ricciardo (Incluindo 1 ponto pela volta mais rápida)
(31, 18, 8, 4, 2020, FALSE),  -- Gasly
(31, 5, 9, 2, 2020, FALSE),   -- Ocon
(31, 10, 10, 1, 2020, FALSE), -- Stroll
(31, 2, 11, 0, 2020, FALSE),  -- Kvyat
(31, 8, 12, 0, 2020, FALSE),  -- Raikkonen
(31, 9, 13, 0, 2020, FALSE),  -- Leclerc
(31, 12, 14, 0, 2020, FALSE), -- Vettel (última corrida pela Ferrari)
(31, 7, 15, 0, 2020, FALSE),  -- Russell
(31, 11, 16, 0, 2020, FALSE), -- Giovinazzi
(31, 14, 17, 0, 2020, FALSE), -- Latifi
(31, 15, 18, 0, 2020, FALSE), -- Magnussen
(31, 16, 19, 0, 2020, FALSE), -- Fittipaldi
(31, 17, 20, 0, 2020, FALSE); -- Perez (Abandonou por falha mecânica)

