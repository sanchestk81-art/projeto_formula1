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

ALTER TABLE corridas  RENAME COLUMN id_cirquitos TO id_circuitos;

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

ALTER TABLE cirquitos RENAME TO CIRCUITOS;


--2020
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

INSERT INTO pilotos (nome, nacionalidade, equipe, pontos, numero_carro) VALUES
-- Estreantes de 2021
('Yuki Tsunoda', 'Japonesa', 'AlphaTauri', 32, 22),
('Mick Schumacher', 'Alemã', 'Haas', 0, 47),
('Nikita Mazepin', 'Russa', 'Haas', 0, 9),
-- Estreantes de 2022
('Guanyu Zhou', 'Chinesa', 'Alfa Romeo', 6, 24),
('Nyck de Vries', 'Holandesa', 'Williams', 2, 45),
-- Estreantes de 2023
('Oscar Piastri', 'Australiana', 'McLaren', 97, 81),
('Logan Sargeant', 'Americana', 'Williams', 1, 2),
-- Estreantes de 2024
('Oliver Bearman', 'Britânica', 'Ferrari', 7, 38),
-- Estreantes de 2025
('Andrea Kimi Antonelli', 'Italiana', 'Mercedes', 0, 12),
('Jack Doohan', 'Australiana', 'Alpine', 0, 7),
('Gabriel Bortoleto', 'Brasileira', 'Sauber', 0, 5),
('Isack Hadjar', 'Francesa', 'RB', 0, 6);
-- Estreantes de 2026
('Rafael Camara', 'Brasileira', 'Haas', 0, 51)

-- circuitos de 2020
INSERT INTO circuitos (id, nome, id_pais, comprimento, voltas) VALUES
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


-- resultado de todos os podiums de 2020
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

--2021
INSERT INTO circuitos (id, nome, id_pais, comprimento, voltas) VALUES
-- Circuitos mantidos de 2020 (IDs 1 a 17)
(32, 'Circuit de Bahrain', 1, 5.41, 57),             -- GP do Bahrein
(33, 'Autodromo Enzo e Dino Ferrari (Imola)', 2, 4.91, 63), -- GP da Emília-Romanha
(34, 'Autódromo Internacional do Algarve (Portimão)', 3, 4.65, 66), -- GP de Portugal
(35, 'Circuit de Barcelona-Catalunya', 4, 4.67, 66), -- GP da Espanha
(36, 'Circuit de Monaco', 5, 3.34, 78),              -- GP de Mônaco
(37, 'Baku City Circuit', 6, 6.00, 51),              -- GP do Azerbaijão
(38, 'Circuit Paul Ricard', 7, 5.84, 53),            -- GP da França
(39, 'Red Bull Ring', 8, 4.32, 71),                  -- GP da Ástria / GP da Estíria
(40, 'Silverstone Circuit', 9, 5.89, 52),            -- GP da Grã-Bretanha
(41, 'Hungaroring', 10, 4.38, 70),                  -- GP da Hungria
(42, 'Circuit de Spa-Francorchamps', 11, 7.00, 44),  -- GP da Bélgica
(43, 'Circuit Zandvoort', 12, 4.25, 72),            -- GP dos Países Baixos (Retorno)
(44, 'Autodromo Nazionale di Monza', 2, 5.79, 53),  -- GP da Itália
(45, 'Sochi Autodrom', 13, 5.85, 53),               -- GP da Rússia
(46, 'Istanbul Park', 14, 5.34, 58),                -- GP da Turquia
(47, 'Circuit of the Americas', 15, 5.51, 56),      -- GP dos Estados Unidos
(48, 'Autódromo Hermanos Rodríguez', 16, 4.30, 71), -- GP da Cidade do México
(49, 'Autódromo José Carlos Pace (Interlagos)', 17, 4.31, 71), -- GP de São Paulo
(50, 'Losail International Circuit', 1, 5.38, 57),  -- GP do Catar (Estreia)
(51, 'Jeddah Corniche Circuit', 18, 6.17, 50),      -- GP da Arábia Saudita (Estreia)
(52, 'Yas Marina Circuit', 19, 5.28, 58);

           -- GP de Abu Dhabi (Modificado em 2021)
--2021
INSERT INTO circuitos (id, nome, id_pais, comprimento, voltas) VALUES
(53, 'Miami International Autodrome', 15, 5.41, 57),       -- GP de Miami (Estreia em 2022)
(54, 'Marina Bay Street Circuit', 20, 5.06, 61),           -- GP de Singapura (Retorno ao calendário em 2022)
(55, 'Suzuka International Racing Course', 21, 5.81, 53),  -- GP do Japão (Retorno ao calendário em 2022)
(56, 'Melbourne Grand Prix Circuit (Albert Park)', 22, 5.28, 58), -- GP da Austrália (Layout modificado / Retorno em 2022)
(57, 'Losail International Circuit', 1, 5.38, 57),         -- GP do Catar (Caso cadastrado especificamente para 2022, se aplicável)
(58, 'Autódromo Internacional de Miami', 15, 5.41, 57);


-- 2022
INSERT INTO circuitos (id, nome, id_pais, comprimento, voltas) VALUES
(59, 'Miami International Autodrome', 15, 5.41, 57),       -- GP de Miami (Estreia em 2022)
(60, 'Melbourne Grand Prix Circuit (Albert Park)', 22, 5.28, 58), -- GP da Austrália (Retorno/Novo Layout)
(61, 'Marina Bay Street Circuit', 20, 5.06, 61),           -- GP de Singapura (Retorno ao calendário)
(62, 'Suzuka International Racing Course', 21, 5.81, 53); 

--2023
INSERT INTO circuitos (id, nome, id_pais, comprimento, voltas) VALUES
(63, 'Circuit Gilles-Villeneuve', 23, 4.36, 70),       -- GP do Canadá (Retorno)
(64, 'Las Vegas Strip Circuit', 15, 6.20, 50);   

-- 2024
INSERT INTO circuitos (id, nome, id_pais, comprimento, voltas) VALUES
(65, 'Shanghai International Circuit', 24, 5.45, 56);

-- 2026
INSERT INTO circuitos (id, nome, id_pais, comprimento, voltas) VALUES
(66, 'Madrid Street Circuit (IFEMA)', 4, 5.47, 55); -- GP da Espanha em Madri (Estreia em 2026) -- GP da China (Retorno ao calendário em 2024)       -- GP de Las Vegas (Estreia em 2023) -- GP do Japão (Retorno ao calendário)     -- (Alternativa caso precise de variação de nome)

-- Resultados das corridas 2021

-- corrida do Bahrein 2021
INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos) VALUES
(32, 1, 1, 25),   -- 1º Lewis Hamilton
(32, 2, 2, 18),   -- 2º Max Verstappen
(32, 3, 3, 16),   -- 3º Valtteri Bottas (+1 ponto de volta rápida)
(32, 4, 4, 12),   -- 4º Lando Norris
(32, 5, 5, 10),   -- 5º Sergio Pérez
(32, 6, 6, 8),    -- 6º Charles Leclerc
(32, 7, 7, 6),    -- 7º Daniel Ricciardo
(32, 8, 8, 4),    -- 8º Carlos Sainz
(32, 9, 9, 2),    -- 9º Yuki Tsunoda
(32, 10, 10, 1),  -- 10º Lance Stroll
(32, 11, 11, 0),  -- 11º Esteban Ocon
(32, 13, 12, 0),  -- 12º Kimi Räikkönen
(32, 14, 13, 0),  -- 13º Antonio Giovinazzi
(32, 15, 14, 0),  -- 14º Sebastian Vettel
(32, 16, 15, 0),  -- 15º Mick Schumacher
(32, 17, 16, 0),  -- 16º Pierre Gasly
(32, 18, 17, 0),  -- 17º Nicholas Latifi (Abandono/Classificado)
(32, 19, 18, 0),  -- 18º George Russell
(32, 20, 19, 0);  -- 19º Nikita Mazepin (Abandono)

-- emilia -romanhaa 2021
IINSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
-- ==========================================
-- GP 1: Sakhir / Bahrein (id_corrida = 32)
-- ==========================================
(32, 1, 1, 25, 2021, 'Não'),
(32, 2, 2, 18, 2021, 'Sim'),
(32, 3, 3, 16, 2021, 'Não'),
(32, 4, 4, 12, 2021, 'Não'),
(32, 5, 5, 10, 2021, 'Não'),
(32, 6, 6, 8, 2021, 'Não'),
(32, 7, 7, 6, 2021, 'Não'),
(32, 8, 8, 4, 2021, 'Não'),
(32, 9, 9, 2, 2021, 'Não'),
(32, 10, 10, 1, 2021, 'Não'),
(32, 11, 11, 0, 2021, 'Não'),
(32, 13, 12, 0, 2021, 'Não'),
(32, 14, 13, 0, 2021, 'Não'),
(32, 15, 14, 0, 2021, 'Não'),
(32, 16, 15, 0, 2021, 'Não'),
(32, 17, 16, 0, 2021, 'Não'),
(32, 18, 17, 0, 2021, 'Não'),
(32, 19, 18, 0, 2021, 'Não'),
(32, 20, 19, 0, 2021, 'Não'),

-- ==========================================
-- GP 2: Imola / Emília-Romanha (id_corrida = 33)
-- ==========================================
(33, 2, 1, 25, 2021, 'Não'),
(33, 1, 2, 19, 2021, 'Sim'),
(33, 3, 3, 15, 2021, 'Não'),
(33, 4, 4, 12, 2021, 'Não'),
(33, 8, 5, 10, 2021, 'Não'),
(33, 6, 6, 8, 2021, 'Não'),
(33, 17, 7, 6, 2021, 'Não'),
(33, 7, 8, 4, 2021, 'Não'),
(33, 10, 9, 2, 2021, 'Não'),
(33, 11, 10, 1, 2021, 'Não'),
(33, 5, 11, 0, 2021, 'Não'),
(33, 12, 12, 0, 2021, 'Não'),
(33, 13, 13, 0, 2021, 'Não'),
(33, 14, 14, 0, 2021, 'Não'),
(33, 15, 15, 0, 2021, 'Não'),
(33, 16, 16, 0, 2021, 'Não'),
(33, 20, 17, 0, 2021, 'Não'),
(33, 18, 18, 0, 2021, 'Não'),
(33, 19, 19, 0, 2021, 'Não'),

-- ==========================================
-- GP 3: Portimão / Portugal (id_corrida = 34)
-- ==========================================
(34, 1, 1, 26, 2021, 'Não'),
(34, 2, 2, 18, 2021, 'Não'),
(34, 3, 3, 15, 2021, 'Sim'),
(34, 5, 4, 12, 2021, 'Não'),
(34, 4, 5, 10, 2021, 'Não'),
(34, 6, 6, 8, 2021, 'Não'),
(34, 11, 7, 6, 2021, 'Não'),
(34, 14, 8, 4, 2021, 'Não'),
(34, 7, 9, 2, 2021, 'Não'),
(34, 17, 10, 1, 2021, 'Não'),
(34, 8, 11, 0, 2021, 'Não'),
(34, 99, 12, 0, 2021, 'Não'),
(34, 5, 13, 0, 2021, 'Não'),
(34, 18, 14, 0, 2021, 'Não'),
(34, 22, 15, 0, 2021, 'Não'),
(34, 63, 16, 0, 2021, 'Não'),
(34, 47, 17, 0, 2021, 'Não'),
(34, 6, 18, 0, 2021, 'Não'),
(34, 9, 19, 0, 2021, 'Não'),
(34, 7, 20, 0, 2021, 'Não'),

-- ==========================================
-- GP 4: Barcelona / Espanha (id_corrida = 35)
-- ==========================================
(35, 1, 1, 25, 2021, 'Sim'),
(35, 2, 2, 18, 2021, 'Não'),
(35, 3, 3, 15, 2021, 'Não'),
(35, 6, 4, 12, 2021, 'Não'),
(35, 5, 5, 10, 2021, 'Não'),
(35, 7, 6, 8, 2021, 'Não'),
(35, 8, 7, 6, 2021, 'Não'),
(35, 4, 8, 4, 2021, 'Não'),
(35, 11, 9, 2, 2021, 'Não'),
(35, 17, 10, 1, 2021, 'Não'),
(35, 18, 11, 0, 2021, 'Não'),
(35, 7, 12, 0, 2021, 'Não'),
(35, 5, 13, 0, 2021, 'Não'),
(35, 63, 14, 0, 2021, 'Não'),
(35, 99, 15, 0, 2021, 'Não'),
(35, 6, 16, 0, 2021, 'Não'),
(35, 14, 17, 0, 2021, 'Não'),
(35, 47, 18, 0, 2021, 'Não'),
(35, 9, 19, 0, 2021, 'Não'),
(35, 22, 20, 0, 2021, 'Não'),

-- ==========================================
-- GP 5: Monte Carlo / Mônaco (id_corrida = 36)
-- ==========================================
(36, 2, 1, 25, 2021, 'Não'),
(36, 8, 2, 18, 2021, 'Não'),
(36, 4, 3, 15, 2021, 'Não'),
(36, 5, 4, 12, 2021, 'Não'),
(36, 15, 5, 10, 2021, 'Não'),
(36, 17, 6, 8, 2021, 'Não'),
(36, 1, 7, 6, 2021, 'Não'),
(36, 10, 8, 4, 2021, 'Não'),
(36, 11, 9, 2, 2021, 'Não'),
(36, 14, 10, 1, 2021, 'Não'),
(36, 13, 11, 0, 2021, 'Não'),
(36, 7, 12, 0, 2021, 'Não'),
(36, 14, 13, 0, 2021, 'Não'),
(36, 19, 14, 0, 2021, 'Não'),
(36, 18, 15, 0, 2021, 'Não'),
(36, 12, 16, 0, 2021, 'Não'),
(36, 20, 17, 0, 2021, 'Não'),
(36, 16, 18, 0, 2021, 'Não'),
(36, 3, 19, 0, 2021, 'Não'),
(36, 6, 20, 0, 2021, 'Sim'),

-- ==========================================
-- GP 6: Baku / Azerbaijão (id_corrida = 37)
-- ==========================================
(37, 5, 1, 25, 2021, 'Não'),
(37, 15, 2, 18, 2021, 'Não'),
(37, 17, 3, 15, 2021, 'Não'),
(37, 6, 4, 12, 2021, 'Sim'),
(37, 4, 5, 10, 2021, 'Não'),
(37, 14, 6, 8, 2021, 'Não'),
(37, 12, 7, 6, 2021, 'Não'),
(37, 8, 8, 4, 2021, 'Não'),
(37, 7, 9, 2, 2021, 'Não'),
(37, 13, 10, 1, 2021, 'Não'),
(37, 14, 11, 0, 2021, 'Não'),
(37, 3, 12, 0, 2021, 'Não'),
(37, 16, 13, 0, 2021, 'Não'),
(37, 20, 14, 0, 2021, 'Não'),
(37, 1, 15, 0, 2021, 'Não'),
(37, 18, 16, 0, 2021, 'Não'),
(37, 2, 17, 0, 2021, 'Não'),
(37, 19, 18, 0, 2021, 'Não'),
(37, 10, 19, 0, 2021, 'Não'),
(37, 11, 20, 0, 2021, 'Não'),

-- ==========================================
-- GP 7: Paul Ricard / França (id_corrida = 38)
-- ==========================================
(38, 2, 1, 25, 2021, 'Sim'),
(38, 1, 2, 18, 2021, 'Não'),
(38, 5, 3, 15, 2021, 'Não'),
(38, 3, 4, 12, 2021, 'Não'),
(38, 4, 5, 10, 2021, 'Não'),
(38, 7, 6, 8, 2021, 'Não'),
(38, 17, 7, 6, 2021, 'Não'),
(38, 14, 8, 4, 2021, 'Não'),
(38, 15, 9, 2, 2021, 'Não'),
(38, 10, 10, 1, 2021, 'Não'),
(38, 8, 11, 0, 2021, 'Não'),
(38, 19, 12, 0, 2021, 'Não'),
(38, 12, 13, 0, 2021, 'Não'),
(38, 11, 14, 0, 2021, 'Não'),
(38, 14, 15, 0, 2021, 'Não'),
(38, 6, 16, 0, 2021, 'Não'),
(38, 13, 17, 0, 2021, 'Não'),
(38, 18, 18, 0, 2021, 'Não'),
(38, 16, 19, 0, 2021, 'Não'),
(38, 20, 20, 0, 2021, 'Não'),

-- ==========================================
-- GP 8: Estíria (id_corrida = 39)
-- ==========================================
(39, 2, 1, 25, 2021, 'Sim'),
(39, 1, 2, 18, 2021, 'Não'),
(39, 3, 3, 15, 2021, 'Não'),
(39, 5, 4, 12, 2021, 'Não'),
(39, 4, 5, 10, 2021, 'Não'),
(39, 8, 6, 8, 2021, 'Não'),
(39, 6, 7, 6, 2021, 'Não'),
(39, 10, 8, 4, 2021, 'Não'),
(39, 14, 9, 2, 2021, 'Não'),
(39, 12, 10, 1, 2021, 'Não'),
(39, 13, 11, 0, 2021, 'Não'),
(39, 15, 12, 0, 2021, 'Não'),
(39, 7, 13, 0, 2021, 'Não'),
(39, 11, 14, 0, 2021, 'Não'),
(39, 14, 15, 0, 2021, 'Não'),
(39, 16, 16, 0, 2021, 'Não'),
(39, 20, 17, 0, 2021, 'Não'),
(39, 18, 18, 0, 2021, 'Não'),
(39, 19, 19, 0, 2021, 'Não'),
(39, 17, 20, 0, 2021, 'Não'),

-- ==========================================
-- GP 9: Spielberg / Áustria (id_corrida = 40)
-- ==========================================
(40, 2, 1, 25, 2021, 'Sim'),
(40, 3, 2, 18, 2021, 'Não'),
(40, 4, 3, 15, 2021, 'Não'),
(40, 1, 4, 12, 2021, 'Não'),
(40, 8, 5, 10, 2021, 'Não'),
(40, 5, 6, 8, 2021, 'Não'),
(40, 7, 7, 6, 2021, 'Não'),
(40, 6, 8, 4, 2021, 'Não'),
(40, 17, 9, 2, 2021, 'Não'),
(40, 14, 10, 1, 2021, 'Não'),
(40, 19, 11, 0, 2021, 'Não'),
(40, 12, 12, 0, 2021, 'Não'),
(40, 10, 13, 0, 2021, 'Não'),
(40, 14, 14, 0, 2021, 'Não'),
(40, 18, 15, 0, 2021, 'Não'),
(40, 13, 16, 0, 2021, 'Não'),
(40, 15, 17, 0, 2021, 'Não'),
(40, 16, 18, 0, 2021, 'Não'),
(40, 20, 19, 0, 2021, 'Não'),
(40, 11, 20, 0, 2021, 'Não'),

-- ==========================================
-- GP 10: Silverstone / Grã-Bretanha (id_corrida = 41)
-- ==========================================
(41, 1, 1, 25, 2021, 'Não'),
(41, 6, 2, 18, 2021, 'Não'),
(41, 3, 3, 15, 2021, 'Não'),
(41, 4, 4, 12, 2021, 'Não'),
(41, 7, 5, 10, 2021, 'Não'),
(41, 8, 6, 8, 2021, 'Não'),
(41, 14, 7, 6, 2021, 'Não'),
(41, 10, 8, 4, 2021, 'Não'),
(41, 11, 9, 2, 2021, 'Não'),
(41, 12, 10, 1, 2021, 'Não'),
(41, 17, 11, 0, 2021, 'Não'),
(41, 14, 12, 0, 2021, 'Não'),
(41, 19, 13, 0, 2021, 'Não'),
(41, 13, 14, 0, 2021, 'Não'),
(41, 18, 15, 0, 2021, 'Não'),
(41, 5, 16, 0, 2021, 'Não'),
(41, 20, 17, 0, 2021, 'Não'),
(41, 16, 18, 0, 2021, 'Não'),
(41, 15, 19, 0, 2021, 'Não'),
(41, 2, 20, 0, 2021, 'Sim'),

-- ==========================================
-- GP 11: Hungaroring / Hungria (id_corrida = 42)
-- ==========================================
(42, 11, 1, 25, 2021, 'Não'),
(42, 1, 2, 18, 2021, 'Sim'),
(42, 8, 3, 15, 2021, 'Não'),
(42, 14, 4, 12, 2021, 'Não'),
(42, 17, 5, 10, 2021, 'Não'),
(42, 12, 6, 8, 2021, 'Não'),
(42, 18, 7, 6, 2021, 'Não'),
(42, 19, 8, 4, 2021, 'Não'),
(42, 10, 9, 2, 2021, 'Não'),
(42, 9, 10, 1, 2021, 'Não'),
(42, 10, 11, 0, 2021, 'Não'),
(42, 14, 12, 0, 2021, 'Não'),
(42, 19, 13, 0, 2021, 'Não'),
(42, 13, 14, 0, 2021, 'Não'),
(42, 18, 15, 0, 2021, 'Não'),
(42, 5, 16, 0, 2021, 'Não'),
(42, 20, 17, 0, 2021, 'Não'),
(42, 16, 18, 0, 2021, 'Não'),
(42, 15, 19, 0, 2021, 'Não'),
(42, 2, 20, 0, 2021, 'Não'),

-- ==========================================
-- GP 12: Spa-Francorchamps / Bélgica (id_corrida = 43)
-- ==========================================
(43, 2, 1, 12.5, 2021, 'Sim'),
(43, 6, 2, 9, 2021, 'Não'),
(43, 4, 3, 7.5, 2021, 'Não'),
(43, 3, 4, 6, 2021, 'Não'),
(43, 5, 5, 5, 2021, 'Não'),
(43, 8, 6, 4, 2021, 'Não'),
(43, 17, 7, 3, 2021, 'Não'),
(43, 10, 8, 2, 2021, 'Não'),
(43, 14, 9, 1, 2021, 'Não'),
(43, 7, 10, 0.5, 2021, 'Não'),
(43, 13, 11, 0, 2021, 'Não'),
(43, 11, 12, 0, 2021, 'Não'),
(43, 12, 13, 0, 2021, 'Não'),
(43, 15, 14, 0, 2021, 'Não'),
(43, 16, 15, 0, 2021, 'Não'),
(43, 18, 16, 0, 2021, 'Não'),
(43, 19, 17, 0, 2021, 'Não'),
(43, 20, 18, 0, 2021, 'Não'),
(43, 9, 19, 0, 2021, 'Não'),
(43, 1, 20, 0, 2021, 'Não'),

-- ==========================================
-- GP 13: Zandvoort / Países Baixos (id_corrida = 44)
-- ==========================================
(44, 2, 1, 25, 2021, 'Sim'),
(44, 1, 2, 18, 2021, 'Não'),
(44, 7, 3, 16, 2021, 'Não'),
(44, 10, 4, 12, 2021, 'Não'),
(44, 8, 5, 10, 2021, 'Não'),
(44, 14, 6, 8, 2021, 'Não'),
(44, 3, 7, 6, 2021, 'Não'),
(44, 17, 8, 4, 2021, 'Não'),
(44, 5, 9, 2, 2021, 'Não'),
(44, 4, 10, 1, 2021, 'Não'),
(44, 11, 11, 0, 2021, 'Não'),
(44, 12, 12, 0, 2021, 'Não'),
(44, 13, 13, 0, 2021, 'Não'),
(44, 15, 14, 0, 2021, 'Não'),
(44, 19, 15, 0, 2021, 'Não'),
(44, 14, 16, 0, 2021, 'Não'),
(44, 18, 17, 0, 2021, 'Não'),
(44, 16, 18, 0, 2021, 'Não'),
(44, 20, 19, 0, 2021, 'Não'),
(44, 16, 20, 0, 2021, 'Não'),

-- ==========================================
-- GP 14: Monza / Itália (id_corrida = 45)
-- ==========================================
(45, 7, 1, 26, 2021, 'Não'),
(45, 8, 2, 18, 2021, 'Não'),
(45, 10, 3, 15, 2021, 'Não'),
(45, 14, 4, 12, 2021, 'Não'),
(45, 11, 5, 10, 2021, 'Não'),
(45, 15, 6, 8, 2021, 'Não'),
(45, 17, 7, 6, 2021, 'Não'),
(45, 19, 8, 4, 2021, 'Não'),
(45, 13, 9, 2, 2021, 'Não'),
(45, 18, 10, 1, 2021, 'Não'),
(45, 12, 11, 0, 2021, 'Não'),
(45, 20, 12, 0, 2021, 'Não'),
(45, 16, 13, 0, 2021, 'Não'),
(45, 5, 14, 0, 2021, 'Não'),
(45, 6, 15, 0, 2021, 'Não'),
(45, 3, 16, 0, 2021, 'Não'),
(45, 1, 17, 0, 2021, 'Não'),
(45, 2, 18, 0, 2021, 'Não'),
(45, 9, 19, 0, 2021, 'Não'),
(45, 4, 20, 0, 2021, 'Não'),

-- ==========================================
-- GP 15: Sóchi / Rússia (id_corrida = 46)
-- ==========================================
(46, 1, 1, 25, 2021, 'Não'),
(46, 3, 2, 18, 2021, 'Não'),
(46, 5, 3, 15, 2021, 'Não'),
(46, 2, 4, 12, 2021, 'Não'),
(46, 14, 5, 10, 2021, 'Não'),
(46, 7, 6, 8, 2021, 'Não'),
(46, 10, 7, 6, 2021, 'Não'),
(46, 4, 8, 4, 2021, 'Não'),
(46, 17, 9, 2, 2021, 'Não'),
(46, 8, 10, 1, 2021, 'Não'),
(46, 11, 11, 0, 2021, 'Não'),
(46, 13, 12, 0, 2021, 'Não'),
(46, 12, 13, 0, 2021, 'Não'),
(46, 19, 14, 0, 2021, 'Não'),
(46, 15, 15, 0, 2021, 'Não'),
(46, 18, 16, 0, 2021, 'Não'),
(46, 16, 17, 0, 2021, 'Não'),
(46, 20, 18, 0, 2021, 'Não'),
(46, 6, 19, 0, 2021, 'Não'),
(46, 9, 20, 0, 2021, 'Não'),

- ==========================================
-- GP 16: Istambul / Turquia (id_corrida = 47)
-- ==========================================
(47, 3, 1, 26, 2021, 'Não'),
(47, 2, 2, 18, 2021, 'Não'),
(47, 11, 3, 15, 2021, 'Não'),
(47, 1, 4, 12, 2021, 'Não'),
(47, 8, 5, 10, 2021, 'Não'),
(47, 7, 6, 8, 2021, 'Não'),
(47, 14, 7, 6, 2021, 'Não'),
(47, 5, 8, 4, 2021, 'Não'),
(47, 10, 9, 2, 2021, 'Não'),
(47, 19, 10, 1, 2021, 'Não'),
(47, 4, 11, 0, 2021, 'Não'),
(47, 17, 12, 0, 2021, 'Não'),
(47, 15, 13, 0, 2021, 'Não'),
(47, 12, 14, 0, 2021, 'Não'),
(47, 13, 15, 0, 2021, 'Não'),
(47, 18, 16, 0, 2021, 'Não'),
(47, 16, 17, 0, 2021, 'Não'),
(47, 20, 18, 0, 2021, 'Não'),
(47, 9, 19, 0, 2021, 'Não'),
(47, 6, 20, 0, 2021, 'Sim'),

-- ==========================================
-- GP 17: Austin / Estados Unidos (id_corrida = 48)
-- ==========================================
(48, 2, 1, 25, 2021, 'Sim'),
(48, 1, 2, 19, 2021, 'Não'),
(48, 5, 3, 15, 2021, 'Não'),
(48, 14, 4, 12, 2021, 'Não'),
(48, 8, 5, 10, 2021, 'Não'),
(48, 4, 6, 8, 2021, 'Não'),
(48, 7, 7, 6, 2021, 'Não'),
(48, 17, 8, 4, 2021, 'Não'),
(48, 10, 9, 2, 2021, 'Não'),
(48, 3, 10, 1, 2021, 'Não'),
(48, 11, 11, 0, 2021, 'Não'),
(48, 12, 12, 0, 2021, 'Não'),
(48, 13, 13, 0, 2021, 'Não'),
(48, 19, 14, 0, 2021, 'Não'),
(48, 18, 15, 0, 2021, 'Não'),
(48, 20, 16, 0, 2021, 'Não'),
(48, 16, 17, 0, 2021, 'Não'),
(48, 6, 18, 0, 2021, 'Não'),
(48, 15, 19, 0, 2021, 'Não'),
(48, 9, 20, 0, 2021, 'Não'),

-- ==========================================
-- GP 18: Cidade do México / México (id_corrida = 49)
-- ==========================================
(49, 2, 1, 25, 2021, 'Não'),
(49, 1, 2, 18, 2021, 'Não'),
(49, 5, 3, 15, 2021, 'Não'),
(49, 10, 4, 12, 2021, 'Não'),
(49, 8, 5, 10, 2021, 'Não'),
(49, 4, 6, 8, 2021, 'Não'),
(49, 7, 7, 6, 2021, 'Não'),
(49, 6, 8, 4, 2021, 'Não'),
(49, 14, 9, 2, 2021, 'Não'),
(49, 17, 10, 1, 2021, 'Não'),
(49, 12, 11, 0, 2021, 'Não'),
(49, 11, 12, 0, 2021, 'Não'),
(49, 13, 13, 0, 2021, 'Não'),
(49, 19, 14, 0, 2021, 'Não'),
(49, 18, 15, 0, 2021, 'Não'),
(49, 16, 16, 0, 2021, 'Não'),
(49, 20, 17, 0, 2021, 'Não'),
(49, 3, 18, 0, 2021, 'Não'),
(49, 15, 19, 0, 2021, 'Não'),
(49, 9, 20, 0, 2021, 'Não'),

-- ==========================================
-- GP 19: Interlagos / São Paulo (id_corrida = 50)
-- ==========================================
(50, 1, 1, 25, 2021, 'Não'),
(50, 2, 2, 19, 2021, 'Não'),
(50, 5, 3, 15, 2021, 'Não'),
(50, 6, 4, 12, 2021, 'Não'),
(50, 3, 5, 10, 2021, 'Não'),
(50, 10, 6, 8, 2021, 'Não'),
(50, 12, 7, 6, 2021, 'Não'),
(50, 8, 8, 4, 2021, 'Não'),
(50, 7, 9, 2, 2021, 'Não'),
(50, 14, 10, 1, 2021, 'Não'),
(50, 11, 11, 0, 2021, 'Não'),
(50, 4, 12, 0, 2021, 'Não'),
(50, 19, 13, 0, 2021, 'Não'),
(50, 13, 14, 0, 2021, 'Não'),
(50, 17, 15, 0, 2021, 'Não'),
(50, 16, 16, 0, 2021, 'Não'),
(50, 18, 17, 0, 2021, 'Não'),
(50, 20, 18, 0, 2021, 'Não'),
(50, 15, 19, 0, 2021, 'Não'),
(50, 9, 20, 0, 2021, 'Não'),

-- ==========================================
-- GP 20: Lusail / Catar (id_corrida = 51)
-- ==========================================
(51, 1, 1, 26, 2021, 'Sim'),
(51, 2, 2, 18, 2021, 'Não'),
(51, 14, 3, 15, 2021, 'Não'),
(51, 5, 4, 12, 2021, 'Não'),
(51, 8, 5, 10, 2021, 'Não'),
(51, 10, 6, 8, 2021, 'Não'),
(51, 11, 7, 6, 2021, 'Não'),
(51, 17, 8, 4, 2021, 'Não'),
(51, 6, 9, 2, 2021, 'Não'),
(51, 4, 10, 1, 2021, 'Não'),
(51, 12, 11, 0, 2021, 'Não'),
(51, 13, 12, 0, 2021, 'Não'),
(51, 19, 13, 0, 2021, 'Não'),
(51, 16, 14, 0, 2021, 'Não'),
(51, 7, 15, 0, 2021, 'Não'),
(51, 20, 16, 0, 2021, 'Não'),
(51, 3, 17, 0, 2021, 'Não'),
(51, 18, 18, 0, 2021, 'Não'),
(51, 15, 19, 0, 2021, 'Não'),
(51, 9, 20, 0, 2021, 'Não'),

-- ==========================================
-- GP 21: Jidá / Arábia Saudita (id_corrida = 52)
-- ==========================================
(52, 1, 1, 26, 2021, 'Sim'),
(52, 2, 2, 18, 2021, 'Não'),
(52, 7, 3, 15, 2021, 'Não'),
(52, 6, 4, 12, 2021, 'Não'),
(52, 10, 5, 10, 2021, 'Não'),
(52, 3, 6, 8, 2021, 'Não'),
(52, 8, 7, 6, 2021, 'Não'),
(52, 12, 8, 4, 2021, 'Não'),
(52, 4, 9, 2, 2021, 'Não'),
(52, 11, 10, 1, 2021, 'Não'),
(52, 17, 11, 0, 2021, 'Não'),
(52, 13, 12, 0, 2021, 'Não'),
(52, 14, 13, 0, 2021, 'Não'),
(52, 15, 14, 0, 2021, 'Não'),
(52, 19, 15, 0, 2021, 'Não'),
(52, 5, 16, 0, 2021, 'Não'),
(52, 18, 17, 0, 2021, 'Não'),
(52, 16, 18, 0, 2021, 'Não'),
(52, 9, 19, 0, 2021, 'Não'),
(52, 20, 20, 0, 2021, 'Não'),

-- ==========================================
-- GP 22: Yas Marina / Abu Dhabi (id_corrida = 53)
-- ==========================================
(53, 2, 1, 26, 2021, 'Não'),
(53, 1, 2, 18, 2021, 'Sim'),
(53, 6, 3, 15, 2021, 'Não'),
(53, 3, 4, 12, 2021, 'Não'),
(53, 5, 5, 10, 2021, 'Não'),
(53, 4, 6, 8, 2021, 'Não'),
(53, 8, 7, 6, 2021, 'Não'),
(53, 17, 8, 4, 2021, 'Não'),
(53, 10, 9, 2, 2021, 'Não'),
(53, 7, 10, 1, 2021, 'Não'),
(53, 11, 11, 0, 2021, 'Não'),
(53, 12, 12, 0, 2021, 'Não'),
(53, 14, 13, 0, 2021, 'Não'),
(53, 13, 14, 0, 2021, 'Não'),
(53, 15, 15, 0, 2021, 'Não'),
(53, 18, 16, 0, 2021, 'Não'),
(53, 19, 17, 0, 2021, 'Não'),
(53, 16, 18, 0, 2021, 'Não'),
(53, 9, 19, 0, 2021, 'Não'),
(53, 20, 20, 0, 2021, 'Não');


------------ 2022
INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
-- ==========================================
-- GP 1: Sakhir / Bahrein (id_corrida = 54)
-- ==========================================
(54, 6, 1, 25, 2022, 'Sim'),   -- Leclerc
(54, 8, 2, 18, 2022, 'Não'),   -- Sainz
(54, 1, 3, 15, 2022, 'Não'),   -- Hamilton
(54, 19, 4, 12, 2022, 'Não'),  -- Russell
(54, 21, 5, 10, 2022, 'Não'),  -- Magnussen
(54, 3, 6, 8, 2022, 'Não'),    -- Bottas
(54, 11, 7, 6, 2022, 'Not'),   -- Ocon
(54, 9, 8, 4, 2022, 'Não'),    -- Tsunoda
(54, 33, 9, 2, 2022, 'Não'),   -- Alonso
(54, 24, 10, 1, 2022, 'Não'),  -- Zhou
(54, 16, 11, 0, 2022, 'Não'),  -- Mick Schumacher
(54, 10, 12, 0, 2022, 'Não'),  -- Stroll
(54, 27, 13, 0, 2022, 'Não'),  -- Hulkenberg
(54, 7, 14, 0, 2022, 'Não'),   -- Ricciardo
(54, 4, 15, 0, 2022, 'Não'),   -- Norris
(54, 18, 16, 0, 2022, 'Não'),  -- Latifi
(54, 23, 17, 0, 2022, 'Não'),  -- Albon
(54, 5, 18, 0, 2022, 'Não'),   -- Perez
(54, 2, 19, 0, 2022, 'Não'),   -- Verstappen
(54, 17, 20, 0, 2022, 'Não'),  -- Gasly

-- ==========================================
-- GP 2: Jidá / Arábia Saudita (id_corrida = 55)
-- ==========================================
(55, 2, 1, 25, 2022, 'Não'),   -- Verstappen
(55, 6, 2, 18, 2022, 'Não'),   -- Leclerc
(55, 8, 3, 15, 2022, 'Não'),   -- Sainz
(55, 5, 4, 12, 2022, 'Sim'),   -- Perez
(55, 19, 5, 10, 2022, 'Não'),  -- Russell
(55, 11, 6, 8, 2022, 'Não'),   -- Ocon
(55, 4, 7, 6, 2022, 'Não'),    -- Norris
(55, 17, 8, 4, 2022, 'Não'),   -- Gasly
(55, 21, 9, 2, 2022, 'Não'),   -- Magnussen
(55, 1, 10, 1, 2022, 'Não'),   -- Hamilton
(55, 24, 11, 0, 2022, 'Não'),  -- Zhou
(55, 27, 12, 0, 2022, 'Não'),  -- Hulkenberg
(55, 10, 13, 0, 2022, 'Não'),  -- Stroll
(55, 23, 14, 0, 2022, 'Não'),  -- Albon
(55, 3, 15, 0, 2022, 'Não'),    -- Bottas
(55, 33, 16, 0, 2022, 'Não'),  -- Alonso
(55, 7, 17, 0, 2022, 'Não'),   -- Ricciardo
(55, 18, 18, 0, 2022, 'Não'),  -- Latifi
(55, 9, 19, 0, 2022, 'Não'),   -- Tsunoda
(55, 16, 20, 0, 2022, 'Não'),  -- Mick Schumacher

-- ==========================================
-- GP 3: Albert Park / Austrália (id_corrida = 56)
-- ==========================================
(56, 6, 1, 25, 2022, 'Sim'),   -- Leclerc
(56, 5, 2, 18, 2022, 'Não'),   -- Perez
(56, 19, 3, 15, 2022, 'Não'),  -- Russell
(56, 1, 4, 12, 2022, 'Não'),   -- Hamilton
(56, 4, 5, 10, 2022, 'Não'),   -- Norris
(56, 7, 6, 8, 2022, 'Não'),    -- Ricciardo
(56, 11, 7, 6, 2022, 'Não'),   -- Ocon
(56, 3, 8, 4, 2022, 'Não'),    -- Bottas
(56, 17, 9, 2, 2022, 'Não'),   -- Gasly
(56, 23, 10, 1, 2022, 'Não'),  -- Albon
(56, 24, 11, 0, 2022, 'Não'),  -- Zhou
(56, 10, 12, 0, 2022, 'Não'),  -- Stroll
(56, 16, 13, 0, 2022, 'Não'),  -- Mick Schumacher
(56, 21, 14, 0, 2022, 'Não'),  -- Magnussen
(56, 9, 15, 0, 2022, 'Não'),   -- Tsunoda
(56, 18, 16, 0, 2022, 'Não'),  -- Latifi
(56, 33, 17, 0, 2022, 'Não'),  -- Alonso
(56, 2, 18, 0, 2022, 'Não'),   -- Verstappen
(56, 15, 19, 0, 2022, 'Não'),  -- Vettel
(56, 8, 20, 0, 2022, 'Não'),   -- Sainz

-- ==========================================
-- GP 4: Imola / Emília-Romanha (id_corrida = 57)
-- ==========================================
(57, 2, 1, 25, 2022, 'Sim'),   -- Verstappen
(57, 5, 2, 18, 2022, 'Não'),   -- Perez
(57, 4, 3, 15, 2022, 'Não'),   -- Norris
(57, 19, 4, 12, 2022, 'Não'),  -- Russell
(57, 3, 5, 10, 2022, 'Não'),   -- Bottas
(57, 6, 6, 8, 2022, 'Não'),    -- Leclerc
(57, 9, 7, 6, 2022, 'Não'),    -- Tsunoda
(57, 15, 8, 4, 2022, 'Não'),   -- Vettel
(57, 21, 9, 2, 2022, 'Não'),   -- Magnussen
(57, 10, 10, 1, 2022, 'Não'),  -- Stroll
(57, 23, 11, 0, 2022, 'Não'),  -- Albon
(57, 17, 12, 0, 2022, 'Não'),  -- Gasly
(57, 1, 13, 0, 2022, 'Não'),   -- Hamilton
(57, 11, 14, 0, 2022, 'Not'),  -- Ocon
(57, 24, 15, 0, 2022, 'Não'),  -- Zhou
(57, 18, 16, 0, 2022, 'Não'),  -- Latifi
(57, 16, 17, 0, 2022, 'Não'),  -- Mick Schumacher
(57, 7, 18, 0, 2022, 'Não'),   -- Ricciardo
(57, 33, 19, 0, 2022, 'Não'),  -- Alonso
(57, 8, 20, 0, 2022, 'Não'),   -- Sainz

-- ==========================================
-- GP 5: Miami (id_corrida = 58)
-- ==========================================
(58, 2, 1, 25, 2022, 'Não'),   -- Verstappen
(58, 6, 2, 18, 2022, 'Sim'),   -- Leclerc
(58, 8, 3, 15, 2022, 'Não'),   -- Sainz
(58, 5, 4, 12, 2022, 'Não'),   -- Perez
(58, 19, 5, 10, 2022, 'Não'),  -- Russell
(58, 1, 6, 8, 2022, 'Não'),    -- Hamilton
(58, 3, 7, 6, 2022, 'Não'),    -- Bottas
(58, 11, 8, 4, 2022, 'Não'),   -- Ocon
(58, 23, 9, 2, 2022, 'Não'),   -- Albon
(58, 10, 10, 1, 2022, 'Não'),  -- Stroll
(58, 33, 11, 0, 2022, 'Não'),  -- Alonso
(58, 9, 12, 0, 2022, 'Não'),   -- Tsunoda
(58, 7, 13, 0, 2022, 'Não'),   -- Ricciardo
(58, 18, 14, 0, 2022, 'Não'),  -- Latifi
(58, 16, 15, 0, 2022, 'Não'),  -- Mick Schumacher
(58, 21, 16, 0, 2022, 'Não'),  -- Magnussen
(58, 15, 17, 0, 2022, 'Não'),  -- Vettel
(58, 17, 18, 0, 2022, 'Não'),  -- Gasly
(58, 4, 19, 0, 2022, 'Não'),   -- Norris
(58, 24, 20, 0, 2022, 'Não');  -- Zhou

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
-- ==========================================
-- GP 6: Barcelona / Espanha (id_corrida = 59)
-- ==========================================
(59, 2, 1, 25, 2022, 'Não'),   -- Verstappen
(59, 5, 2, 18, 2022, 'Não'),   -- Perez
(59, 19, 3, 15, 2022, 'Não'),  -- Russell
(59, 8, 4, 12, 2022, 'Não'),   -- Sainz
(59, 1, 5, 10, 2022, 'Não'),   -- Hamilton
(59, 3, 6, 8, 2022, 'Não'),    -- Bottas
(59, 11, 7, 6, 2022, 'Não'),   -- Ocon
(59, 4, 8, 4, 2022, 'Não'),    -- Norris
(59, 33, 9, 2, 2022, 'Não'),   -- Alonso
(59, 9, 10, 1, 2022, 'Não'),   -- Tsunoda
(59, 15, 11, 0, 2022, 'Não'),  -- Vettel
(59, 7, 12, 0, 2022, 'Não'),   -- Ricciardo
(59, 17, 13, 0, 2022, 'Não'),  -- Gasly
(59, 16, 14, 0, 2022, 'Não'),  -- Mick Schumacher
(59, 10, 15, 0, 2022, 'Não'),  -- Stroll
(59, 18, 16, 0, 2022, 'Não'),  -- Latifi
(59, 21, 17, 0, 2022, 'Não'),  -- Magnussen
(59, 23, 18, 0, 2022, 'Não'),  -- Albon
(59, 24, 19, 0, 2022, 'Não'),  -- Zhou
(59, 6, 20, 0, 2022, 'Sim'),   -- Leclerc

-- ==========================================
-- GP 7: Monte Carlo / Mônaco (id_corrida = 60)
-- ==========================================
(60, 5, 1, 25, 2022, 'Não'),   -- Perez
(60, 8, 2, 18, 2022, 'Não'),   -- Sainz
(60, 2, 3, 15, 2022, 'Não'),   -- Verstappen
(60, 6, 4, 12, 2022, 'Sim'),   -- Leclerc
(60, 19, 5, 10, 2022, 'Não'),  -- Russell
(60, 4, 6, 8, 2022, 'Não'),    -- Norris
(60, 33, 7, 6, 2022, 'Não'),   -- Alonso
(60, 1, 8, 4, 2022, 'Não'),    -- Hamilton
(60, 3, 9, 2, 2022, 'Não'),    -- Bottas
(60, 15, 10, 1, 2022, 'Não'),  -- Vettel
(60, 17, 11, 0, 2022, 'Não'),  -- Gasly
(60, 11, 12, 0, 2022, 'Não'),  -- Ocon
(60, 7, 13, 0, 2022, 'Não'),   -- Ricciardo
(60, 10, 14, 0, 2022, 'Não'),  -- Stroll
(60, 18, 15, 0, 2022, 'Não'),  -- Latifi
(60, 24, 16, 0, 2022, 'Não'),  -- Zhou
(60, 9, 17, 0, 2022, 'Não'),   -- Tsunoda
(60, 23, 18, 0, 2022, 'Não'),  -- Albon
(60, 16, 19, 0, 2022, 'Não'),  -- Mick Schumacher
(60, 21, 20, 0, 2022, 'Não'),  -- Magnussen

-- ==========================================
-- GP 8: Baku / Azerbaijão (id_corrida = 61)
-- ==========================================
(61, 2, 1, 25, 2022, 'Não'),   -- Verstappen
(61, 5, 2, 18, 2022, 'Não'),   -- Perez
(61, 19, 3, 15, 2022, 'Não'),  -- Russell
(61, 1, 4, 12, 2022, 'Não'),   -- Hamilton
(61, 17, 5, 10, 2022, 'Não'),  -- Gasly
(61, 15, 6, 8, 2022, 'Não'),   -- Vettel
(61, 33, 7, 6, 2022, 'Não'),   -- Alonso
(61, 7, 8, 4, 2022, 'Não'),    -- Ricciardo
(61, 4, 9, 2, 2022, 'Não'),    -- Norris
(61, 11, 10, 1, 2022, 'Não'),  -- Ocon
(61, 3, 11, 0, 2022, 'Não'),   -- Bottas
(61, 23, 12, 0, 2022, 'Não'),  -- Albon
(61, 9, 13, 0, 2022, 'Not'),   -- Tsunoda
(61, 16, 14, 0, 2022, 'Não'),  -- Mick Schumacher
(61, 18, 15, 0, 2022, 'Não'),  -- Latifi
(61, 10, 16, 0, 2022, 'Não'),  -- Stroll
(61, 21, 17, 0, 2022, 'Não'),  -- Magnussen
(61, 24, 18, 0, 2022, 'Não'),  -- Zhou
(61, 6, 19, 0, 2022, 'Sim'),   -- Leclerc
(61, 8, 20, 0, 2022, 'Não'),   -- Sainz

-- ==========================================
-- GP 9: Montreal / Canadá (id_corrida = 62)
-- ==========================================
(62, 2, 1, 25, 2022, 'Sim'),   -- Verstappen
(62, 8, 2, 18, 2022, 'Não'),   -- Sainz
(62, 1, 3, 15, 2022, 'Não'),   -- Hamilton
(62, 19, 4, 12, 2022, 'Não'),  -- Russell
(62, 6, 5, 10, 2022, 'Não'),   -- Leclerc
(62, 11, 6, 8, 2022, 'Não'),   -- Ocon
(62, 3, 7, 6, 2022, 'Não'),    -- Bottas
(62, 24, 8, 4, 2022, 'Não'),   -- Zhou
(62, 33, 9, 2, 2022, 'Não'),   -- Alonso
(62, 10, 10, 1, 2022, 'Não'),  -- Stroll
(62, 7, 11, 0, 2022, 'Não'),   -- Ricciardo
(62, 15, 12, 0, 2022, 'Não'),  -- Vettel
(62, 23, 13, 0, 2022, 'Não'),  -- Albon
(62, 17, 14, 0, 2022, 'Não'),  -- Gasly
(62, 4, 15, 0, 2022, 'Não'),   -- Norris
(62, 18, 16, 0, 2022, 'Não'),  -- Latifi
(62, 21, 17, 0, 2022, 'Não'),  -- Magnussen
(62, 9, 18, 0, 2022, 'Não'),   -- Tsunoda
(62, 16, 19, 0, 2022, 'Não'),  -- Mick Schumacher
(62, 5, 20, 0, 2022, 'Não'),   -- Perez

-- ==========================================
-- GP 10: Silverstone / Grã-Bretanha (id_corrida = 63)
-- ==========================================
(63, 8, 1, 25, 2022, 'Sim'),   -- Sainz
(63, 5, 2, 18, 2022, 'Não'),   -- Perez
(63, 1, 3, 15, 2022, 'Não'),   -- Hamilton
(63, 6, 4, 12, 2022, 'Não'),   -- Leclerc
(63, 33, 5, 10, 2022, 'Não'),  -- Alonso
(63, 4, 6, 8, 2022, 'Não'),    -- Norris
(63, 2, 7, 6, 2022, 'Não'),    -- Verstappen
(63, 16, 8, 4, 2022, 'Não'),  -- Mick Schumacher
(63, 15, 9, 2, 2022, 'Não'),   -- Vettel
(63, 21, 10, 1, 2022, 'Não'),  -- Magnussen
(63, 10, 11, 0, 2022, 'Não'),  -- Stroll
(63, 18, 12, 0, 2022, 'Não'),  -- Latifi
(63, 7, 13, 0, 2022, 'Não'),   -- Ricciardo
(63, 9, 14, 0, 2022, 'Não'),   -- Tsunoda
(63, 17, 15, 0, 2022, 'Não'),  -- Gasly
(63, 3, 16, 0, 2022, 'Não'),   -- Bottas
(63, 19, 17, 0, 2022, 'Não'),  -- Russell
(63, 24, 18, 0, 2022, 'Não'),  -- Zhou
(63, 11, 19, 0, 2022, 'Não'),  -- Ocon
(63, 23, 20, 0, 2022, 'Não'),  -- Albon

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
(53, 2, 1, 26, 2021, 'Não'),   -- Max Verstappen (Vencedor + Volta Rápida)
(53, 1, 2, 18, 2021, 'Sim'),   -- Lewis Hamilton (Pole Position)
(53, 6, 3, 15, 2021, 'Não'),   -- Carlos Sainz
(53, 3, 4, 12, 2021, 'Não'),   -- Valtteri Bottas
(53, 5, 5, 10, 2021, 'Não'),   -- Lando Norris
(53, 4, 6, 8, 2021, 'Não'),    -- Yuki Tsunoda (Ajustado conforme ordem do grid original)
(53, 8, 7, 6, 2021, 'Não'),    -- Pierre Gasly
(53, 17, 8, 4, 2021, 'Not'),   -- Fernando Alonso
(53, 10, 9, 2, 2021, 'Não'),   -- Esteban Ocon
(53, 7, 10, 1, 2021, 'Não'),   -- Charles Leclerc
(53, 11, 11, 0, 2021, 'Não'),  -- Sebastian Vettel
(53, 12, 12, 0, 2021, 'Não'),  -- Daniel Ricciardo
(53, 14, 13, 0, 2021, 'Não'),  -- Lance Stroll
(53, 13, 14, 0, 2021, 'Não'),  -- Mick Schumacher
(53, 15, 15, 0, 2021, 'Não'),  -- Nicholas Latifi
(53, 18, 16, 0, 2021, 'Não'),  -- George Russell
(53, 19, 17, 0, 2021, 'Não'),  -- Kimi Räikkönen
(53, 16, 18, 0, 2021, 'Não'),  -- Antonio Giovinazzi
(53, 9, 19, 0, 2021, 'Não'),   -- Sergio Pérez (Abandono/Classificado)
(53, 20, 20, 0, 2021, 'Não');  -- Nikita Mazepin (Abandono)

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
-- ==========================================
-- GP 12: Paul Ricard / França (id_corrida = 65)
-- ==========================================
(65, 2, 1, 25, 2022, 'Não'),   -- Verstappen
(65, 1, 2, 18, 2022, 'Não'),   -- Hamilton
(65, 19, 3, 15, 2022, 'Não'),  -- Russell
(65, 5, 4, 12, 2022, 'Não'),   -- Perez
(65, 33, 5, 10, 2022, 'Não'),  -- Alonso
(65, 4, 6, 8, 2022, 'Não'),    -- Norris
(65, 3, 7, 6, 2022, 'Não'),    -- Bottas
(65, 31, 8, 4, 2022, 'Não'),   -- Ocon
(65, 3, 9, 2, 2022, 'Não'),    -- Ricciardo
(65, 18, 10, 1, 2022, 'Não'),  -- Stroll
(65, 5, 11, 0, 2022, 'Não'),   -- Vettel
(65, 23, 12, 0, 2022, 'Não'),  -- Albon
(65, 10, 13, 0, 2022, 'Não'),  -- Gasly
(65, 24, 14, 0, 2022, 'Não'),  -- Zhou
(65, 6, 15, 0, 2022, 'Sim'),   -- Leclerc
(65, 6, 16, 0, 2022, 'Não'),  -- Mick Schumacher
(65, 20, 17, 0, 2022, 'Não'),  -- Latifi
(65, 22, 18, 0, 2022, 'Não'),  -- Tsunoda
(65, 20, 19, 0, 2022, 'Não'),  -- Magnussen

-- ==========================================
-- GP 13: Hungaroring / Hungria (id_corrida = 66)
-- ==========================================
(66, 2, 1, 25, 2022, 'Não'),   -- Verstappen
(66, 5, 2, 18, 2022, 'Não'),   -- Perez
(66, 1, 3, 15, 2022, 'Não'),   -- Hamilton
(66, 19, 4, 12, 2022, 'Sim'),  -- Russell
(66, 8, 5, 10, 2022, 'Não'),   -- Sainz
(66, 6, 6, 8, 2022, 'Não'),    -- Leclerc
(66, 4, 7, 6, 2022, 'Não'),    -- Norris
(66, 33, 8, 4, 2022, 'Não'),   -- Alonso
(66, 31, 9, 2, 2022, 'Not'),   -- Ocon
(66, 5, 10, 1, 2022, 'Não'),   -- Vettel
(66, 18, 11, 0, 2022, 'Não'),  -- Stroll
(66, 10, 12, 0, 2022, 'Não'),  -- Gasly
(66, 24, 13, 0, 2022, 'Não'),  -- Zhou
(66, 3, 14, 0, 2022, 'Não'),   -- Bottas
(66, 3, 15, 0, 2022, 'Não'),   -- Ricciardo
(66, 22, 16, 0, 2022, 'Não'),  -- Tsunoda
(66, 20, 17, 0, 2022, 'Não'),  -- Albon
(66, 6, 18, 0, 2022, 'Não'),  -- Mick Schumacher
(66, 20, 19, 0, 2022, 'Não'),  -- Magnussen
(66, 20, 20, 0, 2022, 'Não'),  -- Latifi

-- ==========================================
-- GP 14: Spa-Francorchamps / Bélgica (id_corrida = 67)
-- ==========================================
(67, 2, 1, 26, 2022, 'Não'),   -- Verstappen
(67, 5, 2, 18, 2022, 'Não'),   -- Perez
(67, 8, 3, 15, 2022, 'Sim'),   -- Sainz
(67, 6, 4, 12, 2022, 'Não'),   -- Leclerc
(67, 14, 5, 10, 2022, 'Não'),  -- Alonso
(67, 19, 6, 8, 2022, 'Não'),   -- Russell
(67, 16, 7, 6, 2022, 'Não'),   -- Ocon
(67, 5, 8, 4, 2022, 'Não'),    -- Vettel
(67, 10, 9, 2, 2022, 'Não'),   -- Gasly
(67, 18, 10, 1, 2022, 'Não'),  -- Stroll
(67, 4, 11, 0, 2022, 'Não'),   -- Norris
(67, 22, 12, 0, 2022, 'Não'),  -- Tsunoda
(67, 24, 13, 0, 2022, 'Não'),  -- Zhou
(67, 20, 14, 0, 2022, 'Não'),  -- Magnussen
(67, 23, 15, 0, 2022, 'Não'),  -- Albon
(67, 3, 16, 0, 2022, 'Não'),   -- Bottas
(67, 16, 17, 0, 2022, 'Não'),  -- Mick Schumacher
(67, 20, 18, 0, 2022, 'Não'),  -- Latifi
(67, 3, 19, 0, 2022, 'Não'),   -- Ricciardo
(67, 1, 20, 0, 2022, 'Não'),   -- Hamilton

-- ==========================================
-- GP 15: Zandvoort / Países Baixos (id_corrida = 68)
-- ==========================================
(68, 2, 1, 26, 2022, 'Sim'),   -- Verstappen
(68, 6, 2, 18, 2022, 'Não'),   -- Leclerc
(68, 19, 3, 15, 2022, 'Não'),  -- Russell
(68, 5, 4, 12, 2022, 'Não'),   -- Perez
(68, 8, 5, 10, 2022, 'Não'),   -- Sainz
(68, 14, 6, 8, 2022, 'Não'),   -- Alonso
(68, 4, 7, 6, 2022, 'Não'),    -- Norris
(68, 31, 8, 4, 2022, 'Não'),   -- Ocon
(68, 18, 9, 2, 2022, 'Não'),   -- Stroll
(68, 1, 10, 1, 2022, 'Não'),   -- Hamilton
(68, 10, 11, 0, 2022, 'Não'),  -- Gasly
(68, 23, 12, 0, 2022, 'Não'),  -- Albon
(68, 24, 13, 0, 2022, 'Não'),  -- Zhou
(68, 16, 14, 0, 2022, 'Não'),  -- Mick Schumacher
(68, 3, 15, 0, 2022, 'Não'),   -- Bottas
(68, 3, 16, 0, 2022, 'Não'),   -- Ricciardo
(68, 20, 17, 0, 2022, 'Não'),  -- Latifi
(68, 20, 18, 0, 2022, 'Não'),  -- Magnussen
(68, 22, 19, 0, 2022, 'Não'),  -- Tsunoda

-- ==========================================
-- GP 16: Monza / Itália (id_corrida = 69)
-- ==========================================
(69, 2, 1, 25, 2022, 'Não'),   -- Verstappen
(69, 6, 2, 18, 2022, 'Sim'),   -- Leclerc
(69, 1, 3, 15, 2022, 'Não'),   -- Hamilton
(69, 8, 4, 12, 2022, 'Não'),   -- Sainz
(69, 5, 5, 10, 2022, 'Não'),   -- Perez
(69, 19, 6, 8, 2022, 'Não'),   -- Russell
(69, 4, 7, 6, 2022, 'Não'),    -- Norris
(69, 10, 8, 4, 2022, 'Não'),   -- Gasly
(69, 23, 9, 2, 2022, 'Não'),   -- Albon
(69, 31, 10, 1, 2022, 'Não'),  -- Ocon
(69, 24, 11, 0, 2022, 'Não'),  -- Zhou
(69, 3, 12, 0, 2022, 'Não'),   -- Bottas
(69, 20, 13, 0, 2022, 'Não'),  -- Magnussen
(69, 16, 14, 0, 2022, 'Não'),  -- Mick Schumacher
(69, 22, 15, 0, 2022, 'Não'),  -- Tsunoda
(69, 20, 16, 0, 2022, 'Não'),  -- Latifi
(69, 18, 17, 0, 2022, 'Não'),  -- Stroll
(69, 3, 18, 0, 2022, 'Não'),   -- Ricciardo
(69, 14, 19, 0, 2022, 'Não'),  -- Alonso

-- ==========================================
-- GP 17: Singapura (id_corrida = 70)
-- ==========================================
(70, 5, 1, 25, 2022, 'Não'),   -- Perez
(70, 6, 2, 18, 2022, 'Sim'),   -- Leclerc
(70, 8, 3, 15, 2022, 'Não'),   -- Sainz
(70, 19, 4, 12, 2022, 'Não'),  -- Russell
(70, 4, 5, 10, 2022, 'Não'),   -- Norris
(70, 3, 6, 8, 2022, 'Não'),    -- Ricciardo
(70, 18, 7, 6, 2022, 'Não'),   -- Stroll
(70, 2, 8, 4, 2022, 'Não'),    -- Verstappen
(70, 5, 9, 2, 2022, 'Não'),    -- Vettel
(70, 44, 10, 1, 2022, 'Não'),  -- Hamilton
(70, 10, 11, 0, 2022, 'Não'),  -- Gasly
(70, 22, 12, 0, 2022, 'Não'),  -- Bottas
(70, 24, 13, 0, 2022, 'Não'),  -- Zhou
(70, 20, 14, 0, 2022, 'Não'),  -- Magnussen
(70, 20, 15, 0, 2022, 'Não'),  -- Latifi

-- ==========================================
-- GP 18: Suzuka / Japão (id_corrida = 71)
-- ==========================================
(71, 2, 1, 25, 2022, 'Sim'),   -- Verstappen
(71, 5, 2, 18, 2022, 'Não'),   -- Perez
(71, 6, 3, 15, 2022, 'Não'),   -- Leclerc
(71, 8, 4, 12, 2022, 'Não'),   -- Sainz
(71, 33, 5, 10, 2022, 'Não'),  -- Alonso
(71, 19, 6, 8, 2022, 'Não'),   -- Russell
(71, 4, 7, 6, 2022, 'Não'),    -- Norris
(71, 3, 8, 4, 2022, 'Não'),    -- Ricciardo
(71, 18, 9, 2, 2022, 'Não'),   -- Stroll
(71, 22, 10, 1, 2022, 'Não'),  -- Tsunoda
(71, 31, 11, 0, 2022, 'Não'),  -- Ocon
(71, 24, 12, 0, 2022, 'Não'),  -- Zhou
(71, 10, 13, 0, 2022, 'Não'),  -- Gasly
(71, 23, 14, 0, 2022, 'Não'),  -- Albon
(71, 44, 15, 0, 2022, 'Não'),  -- Hamilton
(71, 20, 16, 0, 2022, 'Não'),  -- Magnussen
(71, 16, 17, 0, 2022, 'Não'),  -- Mick Schumacher
(71, 20, 18, 0, 2022, 'Não'),  -- Latifi

-- ==========================================
-- GP 19: Austin / Estados Unidos (id_corrida = 72)
-- ==========================================
(72, 2, 1, 25, 2022, 'Não'),   -- Verstappen
(72, 44, 2, 18, 2022, 'Não'),  -- Hamilton
(72, 16, 3, 15, 2022, 'Não'),  -- Leclerc
(72, 5, 4, 12, 2022, 'Não'),   -- Perez
(72, 19, 5, 10, 2022, 'Não'),  -- Russell
(72, 4, 6, 8, 2022, 'Não'),    -- Norris
(72, 3, 7, 6, 2022, 'Não'),    -- Alonso
(72, 31, 8, 4, 2022, 'Not'),   -- Ocon
(72, 3, 9, 2, 2022, 'Não'),    -- Ricciardo
(72, 22, 10, 1, 2022, 'Não'),  -- Tsunoda
(72, 24, 11, 0, 2022, 'Não'),  -- Zhou
(72, 23, 12, 0, 2022, 'Não'),  -- Albon
(72, 10, 13, 0, 2022, 'Não'),  -- Gasly
(72, 20, 14, 0, 2022, 'Não'),  -- Magnussen
(72, 16, 15, 0, 2022, 'Não'),  -- Mick Schumacher
(72, 3, 16, 0, 2022, 'Não'),   -- Bottas
(72, 20, 17, 0, 2022, 'Não'),  -- Latifi
(72, 18, 18, 0, 2022, 'Não'),  -- Stroll
(72, 8, 19, 0, 2022, 'Sim'),   -- Sainz

-- ==========================================
-- GP 20: Cidade do México (id_corrida = 73)
-- ==========================================
(73, 2, 1, 25, 2022, 'Não'),   -- Verstappen
(73, 44, 2, 18, 2022, 'Não'),  -- Hamilton
(73, 5, 3, 15, 2022, 'Sim'),   -- Perez
(73, 6, 4, 12, 2022, 'Não'),   -- Leclerc
(73, 8, 5, 10, 2022, 'Não'),   -- Sainz
(73, 3, 6, 8, 2022, 'Não'),    -- Ricciardo
(73, 31, 7, 6, 2022, 'Não'),   -- Ocon
(73, 4, 8, 4, 2022, 'Não'),    -- Norris
(73, 7, 9, 2, 2022, 'Não'),    -- Bottas
(73, 10, 10, 1, 2022, 'Não'),  -- Gasly
(73, 23, 11, 0, 2022, 'Não'),  -- Albon
(73, 24, 12, 0, 2022, 'Não'),  -- Zhou
(73, 5, 13, 0, 2022, 'Não'),   -- Vettel
(73, 18, 14, 0, 2022, 'Não'),  -- Stroll
(73, 19, 15, 0, 2022, 'Não'),  -- Russell
(73, 20, 16, 0, 2022, 'Não'),  -- Magnussen
(73, 20, 17, 0, 2022, 'Não'),  -- Latifi
(73, 16, 18, 0, 2022, 'Não'),  -- Mick Schumacher
(73, 22, 19, 0, 2022, 'Não'),  -- Tsunoda

-- ==========================================
-- GP 21: São Paulo / Interlagos (id_corrida = 74)
-- ==========================================
(74, 19, 1, 26, 2022, 'Não'),  -- Russell
(74, 44, 2, 18, 2022, 'Não'),  -- Hamilton
(74, 5, 3, 15, 2022, 'Não'),   -- Perez
(74, 8, 4, 12, 2022, 'Não'),   -- Sainz
(74, 6, 5, 10, 2022, 'Não'),   -- Leclerc
(74, 2, 6, 8, 2022, 'Não'),    -- Verstappen
(74, 33, 7, 6, 2022, 'Não'),   -- Alonso
(74, 3, 8, 4, 2022, 'Não'),    -- Bottas
(74, 18, 9, 2, 2022, 'Não'),   -- Stroll
(74, 31, 10, 1, 2022, 'Not'),  -- Ocon
(74, 4, 11, 0, 2022, 'Não'),   -- Norris
(74, 24, 12, 0, 2022, 'Não'),  -- Zhou
(74, 21, 13, 0, 2022, 'Não'),  -- Magnussen
(74, 16, 14, 0, 2022, 'Não'),  -- Mick Schumacher
(74, 10, 15, 0, 2022, 'Não'),  -- Gasly
(74, 23, 16, 0, 2022, 'Não'),  -- Albon
(74, 22, 17, 0, 2022, 'Não'),  -- Tsunoda
(74, 20, 18, 0, 2022, 'Não'),  -- Latifi

-- ==========================================
-- GP 22: Yas Marina / Abu Dhabi (id_corrida = 75)
-- ==========================================
(75, 2, 1, 25, 2022, 'Sim'),   -- Verstappen
(75, 16, 2, 18, 2022, 'Não'),  -- Leclerc
(75, 5, 3, 15, 2022, 'Não'),   -- Perez
(75, 44, 4, 12, 2022, 'Não'),  -- Hamilton
(75, 8, 5, 10, 2022, 'Não'),   -- Sainz
(75, 19, 6, 8, 2022, 'Não'),   -- Russell
(75, 4, 7, 6, 2022, 'Não'),    -- Norris
(75, 33, 8, 4, 2022, 'Não'),   -- Alonso
(75, 31, 9, 2, 2022, 'Not'),   -- Ocon
(75, 18, 10, 1, 2022, 'Não'),  -- Stroll
(75, 3, 11, 0, 2022, 'Não'),   -- Bottas
(75, 5, 12, 0, 2022, 'Não'),   -- Vettel
(75, 3, 13, 0, 2022, 'Não'),   -- Ricciardo
(75, 23, 14, 0, 2022, 'Não'),  -- Albon
(75, 24, 15, 0, 2022, 'Não'),  -- Zhou
(75, 10, 16, 0, 2022, 'Não'),  -- Gasly
(75, 22, 17, 0, 2022, 'Não'),  -- Tsunoda
(75, 20, 18, 0, 2022, 'Não'),  -- Magnussen
(75, 20, 19, 0, 2022, 'Não');  -- Latifi

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
-- ==========================================
-- GP 1: Sakhir / Bahrein (id_corrida = 76)
-- ==========================================
(76, 2, 1, 25, 2023, 'Sim'),   -- Verstappen
(76, 5, 2, 18, 2023, 'Não'),   -- Perez
(76, 33, 3, 15, 2023, 'Não'),  -- Alonso
(76, 8, 4, 12, 2023, 'Não'),   -- Sainz
(76, 1, 5, 10, 2023, 'Not'),   -- Hamilton
(76, 18, 6, 8, 2023, 'Não'),   -- Stroll
(76, 19, 7, 6, 2023, 'Não'),   -- Russell
(76, 3, 8, 4, 2023, 'Não'),    -- Bottas
(76, 10, 9, 2, 2023, 'Não'),   -- Gasly
(76, 23, 10, 1, 2023, 'Não'),  -- Albon
(76, 22, 11, 0, 2023, 'Não'),  -- Tsunoda
(76, 2, 12, 0, 2023, 'Não'),   -- Sargeant
(76, 21, 13, 0, 2023, 'Não'),  -- De Vries
(76, 27, 14, 0, 2023, 'Não'),  -- Hulkenberg
(76, 24, 15, 0, 2023, 'Não'),  -- Zhou
(76, 4, 16, 0, 2023, 'Não'),   -- Norris
(76, 31, 17, 0, 2023, 'Não'),  -- Ocon
(76, 6, 18, 0, 2023, 'Não'),   -- Leclerc
(76, 81, 19, 0, 2023, 'Não'),  -- Piastri
(76, 20, 20, 0, 2023, 'Não'),  -- Magnussen

-- ==========================================
-- GP 2: Jidá / Arábia Saudita (id_corrida = 77)
-- ==========================================
(77, 5, 1, 25, 2023, 'Sim'),   -- Perez
(77, 2, 2, 18, 2023, 'Não'),   -- Verstappen
(77, 33, 3, 15, 2023, 'Não'),  -- Alonso
(77, 19, 4, 12, 2023, 'Não'),  -- Russell
(77, 1, 5, 10, 2023, 'Não'),   -- Hamilton
(77, 8, 6, 8, 2023, 'Não'),    -- Sainz
(77, 6, 7, 6, 2023, 'Não'),    -- Leclerc
(77, 31, 8, 4, 2023, 'Não'),   -- Ocon
(77, 10, 9, 2, 2023, 'Não'),   -- Gasly
(77, 20, 10, 1, 2023, 'Não'),  -- Magnussen
(77, 22, 11, 0, 2023, 'Não'),  -- Tsunoda
(77, 27, 12, 0, 2023, 'Não'),  -- Hulkenberg
(77, 24, 13, 0, 2023, 'Não'),  -- Zhou
(77, 21, 14, 0, 2023, 'Não'),  -- De Vries
(77, 81, 15, 0, 2023, 'Não'),  -- Piastri
(77, 2, 16, 0, 2023, 'Não'),   -- Sargeant
(77, 4, 17, 0, 2023, 'Não'),   -- Norris
(77, 3, 18, 0, 2023, 'Não'),   -- Bottas
(77, 23, 19, 0, 2023, 'Não'),  -- Albon
(77, 18, 20, 0, 2023, 'Não'),  -- Stroll

-- ==========================================
-- GP 3: Albert Park / Austrália (id_corrida = 78)
-- ==========================================
(78, 2, 1, 25, 2023, 'Sim'),   -- Verstappen
(78, 1, 2, 18, 2023, 'Não'),   -- Hamilton
(78, 33, 3, 15, 2023, 'Não'),  -- Alonso
(78, 18, 4, 12, 2023, 'Não'),  -- Stroll
(78, 5, 5, 10, 2023, 'Não'),   -- Perez
(78, 4, 6, 8, 2023, 'Não'),    -- Norris
(78, 27, 7, 6, 2023, 'Não'),   -- Hulkenberg
(78, 81, 8, 4, 2023, 'Não'),  -- Piastri
(78, 24, 9, 2, 2023, 'Não'),   -- Zhou
(78, 22, 10, 1, 2023, 'Não'),  -- Tsunoda
(78, 3, 11, 0, 2023, 'Não'),   -- Bottas
(78, 8, 12, 0, 2023, 'Não'),   -- Sainz
(78, 10, 13, 0, 2023, 'Não'),  -- Gasly
(78, 31, 14, 0, 2023, 'Not'),   -- Ocon
(78, 21, 15, 0, 2023, 'Não'),  -- De Vries
(78, 2, 16, 0, 2023, 'Não'),   -- Sargeant
(78, 20, 17, 0, 2023, 'Não'),  -- Magnussen
(78, 19, 18, 0, 2023, 'Não'),  -- Russell
(78, 23, 19, 0, 2023, 'Não'),  -- Albon
(78, 6, 20, 0, 2023, 'Não'),   -- Leclerc

-- ==========================================
-- GP 4: Baku / Azerbaijão (id_corrida = 79)
-- ==========================================
(79, 5, 1, 25, 2023, 'Não'),   -- Perez
(79, 2, 2, 18, 2023, 'Não'),   -- Verstappen
(79, 6, 3, 15, 2023, 'Sim'),   -- Leclerc
(79, 33, 4, 12, 2023, 'Não'),  -- Alonso
(79, 8, 5, 10, 2023, 'Não'),   -- Sainz
(79, 1, 6, 8, 2023, 'Não'),    -- Hamilton
(79, 18, 7, 6, 2023, 'Não'),   -- Stroll
(79, 19, 8, 4, 2023, 'Não'),   -- Russell
(79, 4, 9, 2, 2023, 'Não'),    -- Norris
(79, 22, 10, 1, 2023, 'Não'),  -- Tsunoda
(79, 81, 11, 0, 2023, 'Não'),  -- Piastri
(79, 23, 12, 0, 2023, 'Não'),  -- Albon
(79, 20, 13, 0, 2023, 'Não'),  -- Magnussen
(79, 10, 14, 0, 2023, 'Não'),  -- Gasly
(79, 31, 15, 0, 2023, 'Não'),  -- Ocon
(79, 2, 16, 0, 2023, 'Não'),   -- Sargeant
(79, 27, 17, 0, 2023, 'Não'),  -- Hulkenberg
(79, 3, 18, 0, 2023, 'Não'),   -- Bottas
(79, 24, 19, 0, 2023, 'Não'),  -- Zhou
(79, 21, 20, 0, 2023, 'Não'),  -- De Vries

-- ==========================================
-- GP 5: Miami (id_corrida = 80)
-- ==========================================
(80, 2, 1, 25, 2023, 'Não'),   -- Verstappen
(80, 5, 2, 18, 2023, 'Sim'),   -- Perez
(80, 33, 3, 15, 2023, 'Não'),  -- Alonso
(80, 19, 4, 12, 2023, 'Não'),  -- Russell
(80, 8, 5, 10, 2023, 'Não'),   -- Sainz
(80, 1, 6, 8, 2023, 'Não'),    -- Hamilton
(80, 6, 7, 6, 2023, 'Não'),    -- Leclerc
(80, 10, 8, 4, 2023, 'Não'),   -- Gasly
(80, 31, 9, 2, 2023, 'Não'),   -- Ocon
(80, 20, 10, 1, 2023, 'Não'),  -- Magnussen
(80, 22, 11, 0, 2023, 'Não'),  -- Tsunoda
(80, 18, 12, 0, 2023, 'Não'),  -- Stroll
(80, 3, 13, 0, 2023, 'Não'),   -- Bottas
(80, 23, 14, 0, 2023, 'Não'),  -- Albon
(80, 27, 15, 0, 2023, 'Não'),  -- Hulkenberg
(80, 24, 16, 0, 2023, 'Não'),  -- Zhou
(80, 4, 17, 0, 2023, 'Não'),   -- Norris
(80, 21, 18, 0, 2023, 'Não'),  -- De Vries
(80, 81, 19, 0, 2023, 'Não'),  -- Piastri
(80, 2, 20, 0, 2023, 'Não'),   -- Sargeant

-- ==========================================
-- GP 6: Monte Carlo / Mônaco (id_corrida = 81)
-- ==========================================
(81, 2, 1, 25, 2023, 'Sim'),   -- Verstappen
(81, 33, 2, 18, 2023, 'Não'),  -- Alonso
(81, 31, 3, 15, 2023, 'Não'),  -- Ocon
(81, 1, 4, 12, 2023, 'Não'),   -- Hamilton
(81, 19, 5, 10, 2023, 'Não'),  -- Russell
(81, 6, 6, 8, 2023, 'Não'),    -- Leclerc
(81, 10, 7, 6, 2023, 'Não'),   -- Gasly
(81, 8, 8, 4, 2023, 'Não'),    -- Sainz
(81, 4, 9, 2, 2023, 'Não'),    -- Norris
(81, 81, 10, 1, 2023, 'Não'),  -- Piastri
(81, 3, 11, 0, 2023, 'Não'),   -- Bottas
(81, 21, 12, 0, 2023, 'Não'),  -- De Vries
(81, 24, 13, 0, 2023, 'Não'),  -- Zhou
(81, 23, 14, 0, 2023, 'Não'),  -- Albon
(81, 22, 15, 0, 2023, 'Não'),  -- Tsunoda
(81, 5, 16, 0, 2023, 'Não'),   -- Perez
(81, 27, 17, 0, 2023, 'Não'),  -- Hulkenberg
(81, 2, 18, 0, 2023, 'Não'),   -- Sargeant
(81, 20, 19, 0, 2023, 'Não'),  -- Magnussen
(81, 18, 20, 0, 2023, 'Não'),  -- Stroll

-- ==========================================
-- GP 7: Barcelona / Espanha (id_corrida = 82)
-- ==========================================
(82, 2, 1, 25, 2023, 'Sim'),   -- Verstappen
(82, 1, 2, 18, 2023, 'Não'),   -- Hamilton
(82, 19, 3, 15, 2023, 'Não'),  -- Russell
(82, 5, 4, 12, 2023, 'Não'),   -- Perez
(82, 8, 5, 10, 2023, 'Não'),   -- Sainz
(82, 18, 6, 8, 2023, 'Não'),   -- Stroll
(82, 33, 7, 6, 2023, 'Não'),   -- Alonso
(82, 31, 8, 4, 2023, 'Não'),   -- Ocon
(82, 24, 9, 2, 2023, 'Não'),   -- Zhou
(82, 10, 10, 1, 2023, 'Não'),  -- Gasly
(82, 6, 11, 0, 2023, 'Não'),   -- Leclerc
(82, 22, 12, 0, 2023, 'Não'),  -- Tsunoda
(82, 81, 13, 0, 2023, 'Não'),  -- Piastri
(82, 21, 14, 0, 2023, 'Não'),  -- De Vries
(82, 27, 15, 0, 2023, 'Não'),  -- Hulkenberg
(82, 23, 16, 0, 2023, 'Não'),  -- Albon
(82, 4, 17, 0, 2023, 'Não'),   -- Norris
(82, 20, 18, 0, 2023, 'Não'),  -- Magnussen
(82, 3, 19, 0, 2023, 'Não'),   -- Bottas
(82, 2, 20, 0, 2023, 'Não'),   -- Sargeant

-- ==========================================
-- GP 8: Montreal / Canadá (id_corrida = 83)
-- ==========================================
(83, 2, 1, 25, 2023, 'Sim'),   -- Verstappen
(83, 33, 2, 18, 2023, 'Não'),  -- Alonso
(83, 1, 3, 15, 2023, 'Não'),   -- Hamilton
(83, 6, 4, 12, 2023, 'Não'),   -- Leclerc
(83, 8, 5, 10, 2023, 'Não'),   -- Sainz
(83, 5, 6, 8, 2023, 'Não'),    -- Perez
(83, 23, 7, 6, 2023, 'Não'),   -- Albon
(83, 31, 8, 4, 2023, 'Não'),   -- Ocon
(83, 18, 9, 2, 2023, 'Não'),   -- Stroll
(83, 3, 10, 1, 2023, 'Não'),   -- Bottas
(83, 4, 11, 0, 2023, 'Não'),   -- Norris
(83, 10, 12, 0, 2023, 'Não'),  -- Gasly
(83, 81, 13, 0, 2023, 'Não'),  -- Piastri
(83, 22, 14, 0, 2023, 'Não'),  -- Tsunoda
(83, 27, 15, 0, 2023, 'Não'),  -- Hulkenberg
(83, 24, 16, 0, 2023, 'Não'),  -- Zhou
(83, 20, 17, 0, 2023, 'Não'),  -- Magnussen
(83, 21, 18, 0, 2023, 'Não'),  -- De Vries
(83, 19, 19, 0, 2023, 'Não'),  -- Russell
(83, 2, 20, 0, 2023, 'Não'),   -- Sargeant

-- ==========================================
-- GP 9: Spielberg / Áustria (id_corrida = 84)
-- ==========================================
(84, 2, 1, 25, 2023, 'Sim'),   -- Verstappen
(84, 6, 2, 18, 2023, 'Não'),   -- Leclerc
(84, 5, 3, 15, 2023, 'Não'),   -- Perez
(84, 4, 4, 12, 2023, 'Não'),   -- Norris
(84, 33, 5, 10, 2023, 'Não'),  -- Alonso
(84, 8, 6, 8, 2023, 'Não'),    -- Sainz
(84, 19, 7, 6, 2023, 'Não'),   -- Russell
(84, 1, 8, 4, 2023, 'Não'),    -- Hamilton
(84, 18, 9, 2, 2023, 'Não'),   -- Stroll
(84, 10, 10, 1, 2023, 'Não'),  -- Gasly
(84, 23, 11, 0, 2023, 'Não'),  -- Albon
(84, 24, 12, 0, 2023, 'Não'),  -- Zhou
(84, 31, 13, 0, 2023, 'Não'),  -- Ocon
(84, 21, 14, 0, 2023, 'Não'),  -- De Vries
(84, 4, 15, 0, 2023, 'Não'),   -- Lando Norris (repetido no log original, padronizado)
(84, 3, 16, 0, 2023, 'Não'),   -- Bottas
(84, 81, 17, 0, 2023, 'Não'),  -- Piastri
(84, 22, 18, 0, 2023, 'Não'),  -- Tsunoda
(84, 20, 19, 0, 2023, 'Não'),  -- Magnussen
(84, 27, 20, 0, 2023, 'Não'),  -- Hulkenberg

-- ==========================================
-- GP 10: Silverstone / Grã-Bretanha (id_corrida = 85)
-- ==========================================
(85, 2, 1, 25, 2023, 'Sim'),   -- Verstappen
(85, 4, 2, 18, 2023, 'Não'),   -- Norris
(85, 1, 3, 15, 2023, 'Não'),   -- Hamilton
(85, 81, 4, 12, 2023, 'Not'),  -- Piastri
(85, 19, 5, 10, 2023, 'Não'),  -- Russell
(85, 5, 6, 8, 2023, 'Não'),    -- Perez
(85, 33, 7, 6, 2023, 'Não'),   -- Alonso
(85, 23, 8, 4, 2023, 'Não'),   -- Albon
(85, 6, 9, 2, 2023, 'Não'),    -- Leclerc
(85, 8, 10, 1, 2023, 'Não'),   -- Sainz
(85, 2, 11, 0, 2023, 'Não'),   -- Sargeant
(85, 3, 12, 0, 2023, 'Não'),   -- Bottas
(85, 27, 13, 0, 2023, 'Não'),  -- Hulkenberg
(85, 18, 14, 0, 2023, 'Não'),  -- Stroll
(85, 24, 15, 0, 2023, 'Não'),  -- Zhou
(85, 22, 16, 0, 2023, 'Não'),  -- Tsunoda
(85, 21, 17, 0, 2023, 'Não'),  -- De Vries
(85, 10, 18, 0, 2023, 'Não'),  -- Gasly
(85, 31, 19, 0, 2023, 'Não'),  -- Ocon
(85, 20, 20, 0, 2023, 'Não'),  -- Magnussen

INSERT INTO resultados (id_corrida, id_piloto, posicao, pontos, ano, pole_position) VALUES
-- ==========================================
-- GP 11: Hungaroring / Hungria (id_corrida = 86) - Completo
-- ==========================================
(86, 2, 1, 25, 2023, 'Não'),   -- Verstappen
(86, 4, 2, 18, 2023, 'Não'),   -- Norris
(86, 5, 3, 15, 2023, 'Não'),   -- Perez
(86, 1, 4, 12, 2023, 'Sim'),   -- Hamilton
(86, 81, 5, 10, 2023, 'Não'),  -- Piastri
(86, 19, 6, 8, 2023, 'Não'),   -- Russell
(86, 6, 7, 6, 2023, 'Não'),    -- Leclerc
(86, 8, 8, 4, 2023, 'Não'),    -- Sainz
(86, 14, 9, 2, 2023, 'Não'),   -- Alonso
(86, 18, 10, 1, 2023, 'Não'),  -- Stroll
(86, 23, 11, 0, 2023, 'Não'),  -- Albon
(86, 77, 12, 0, 2023, 'Não'),  -- Bottas
(86, 24, 13, 0, 2023, 'Não'),  -- Zhou
(86, 27, 14, 0, 2023, 'Não'),  -- Hulkenberg
(86, 22, 15, 0, 2023, 'Não'),  -- Tsunoda
(86, 3, 16, 0, 2023, 'Não'),   -- Ricciardo
(86, 20, 17, 0, 2023, 'Não'),  -- Magnussen
(86, 2, 18, 0, 2023, 'Não'),   -- Sargeant
(86, 10, 19, 0, 2023, 'Não'),  -- Gasly
(86, 31, 20, 0, 2023, 'Não');  -- Ocon
