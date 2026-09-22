-- CRIAÇÃO DAS TABELAS

CREATE TABLE paises (
    id INTEGER NOT NULL,
    nome_pais VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE equipes (
    id INTEGER NOT NULL,
    nome_equipe VARCHAR(255) NOT NULL,
    nacionalidade VARCHAR(255) NOT NULL,
    ano_fundado INTEGER NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE pilotos (
    id INTEGER NOT NULL,
    nome_piloto VARCHAR(200) NOT NULL,
    nacionalidade VARCHAR(255) NOT NULL,
    equipe_id INTEGER NOT NULL,
    ano_entrou INTEGER NOT NULL,
    numero_car INTEGER NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE circuitos (
    id INTEGER NOT NULL,
    nome_circuito VARCHAR(100) NOT NULL,
    pais_id INTEGER NOT NULL,
    qtd_curvas INTEGER NOT NULL,
    km NUMERIC NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE corridas (
    id INTEGER NOT NULL,
    data TIMESTAMP NOT NULL,
    circuito_id INTEGER NOT NULL,
    pole_position_id INTEGER NOT NULL,
    primeiro_lugar_id INTEGER NOT NULL,
    segundo_lugar_id INTEGER NOT NULL,
    terceiro_lugar_id INTEGER NOT NULL,
    tempo_volta_rapida TIME NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE pontuacao_pilotos (
    id INTEGER NOT NULL,
    corrida_id INTEGER NOT NULL,
    piloto_id INTEGER NOT NULL,
    colocacao INTEGER NOT NULL,
    qtd_pontos INTEGER NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE pontuacao_equipes (
    id INTEGER NOT NULL,
    corrida_id INTEGER NOT NULL,
    qtd_pontos INTEGER NOT NULL,
    equipe_id INTEGER NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE pilotos_equipes (
    id INTEGER NOT NULL,
    piloto_id INTEGER NOT NULL,
    equipe_id INTEGER NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE carro (
    id INTEGER NOT NULL,
    pilotos_id INTEGER NOT NULL,
    equipe_id INTEGER,
    PRIMARY KEY (id)
);

CREATE TABLE wc (
    id INTEGER NOT NULL,
    piloto_id INTEGER NOT NULL,
    equipe_id INTEGER NOT NULL,
    carro_id INTEGER NOT NULL,
    pontuacao INTEGER NOT NULL,
    PRIMARY KEY (id)
);


-- CHAVES ESTRANGEIRAS

ALTER TABLE circuitos
ADD FOREIGN KEY (pais_id) REFERENCES paises(id);

ALTER TABLE corridas
ADD FOREIGN KEY (circuito_id) REFERENCES circuitos(id);

ALTER TABLE pilotos
ADD FOREIGN KEY (equipe_id) REFERENCES equipes(id);

ALTER TABLE pilotos_equipes
ADD FOREIGN KEY (piloto_id) REFERENCES pilotos(id);

ALTER TABLE pilotos_equipes
ADD FOREIGN KEY (equipe_id) REFERENCES equipes(id);

ALTER TABLE pontuacao_pilotos
ADD FOREIGN KEY (corrida_id) REFERENCES corridas(id);

ALTER TABLE pontuacao_pilotos
ADD FOREIGN KEY (piloto_id) REFERENCES pilotos(id);

ALTER TABLE pontuacao_equipes
ADD FOREIGN KEY (corrida_id) REFERENCES corridas(id);

ALTER TABLE pontuacao_equipes
ADD FOREIGN KEY (equipe_id) REFERENCES equipes(id);

ALTER TABLE carro
ADD FOREIGN KEY (pilotos_id) REFERENCES pilotos(id);

ALTER TABLE carro
ADD FOREIGN KEY (equipe_id) REFERENCES equipes(id);

ALTER TABLE wc
ADD FOREIGN KEY (piloto_id) REFERENCES pilotos(id);

ALTER TABLE wc
ADD FOREIGN KEY (equipe_id) REFERENCES equipes(id);

ALTER TABLE wc
ADD FOREIGN KEY (carro_id) REFERENCES carro(id);

ALTER TABLE corridas
ADD FOREIGN KEY (pole_position_id) REFERENCES pilotos(id);

ALTER TABLE corridas
ADD FOREIGN KEY (primeiro_lugar_id) REFERENCES pilotos(id);

ALTER TABLE corridas
ADD FOREIGN KEY (segundo_lugar_id) REFERENCES pilotos(id);

ALTER TABLE corridas
ADD FOREIGN KEY (terceiro_lugar_id) REFERENCES pilotos(id);


-- INSERINDO AS EQUIPES

INSERT INTO equipes
(id, nome_equipe, nacionalidade, ano_fundado)
VALUES
(1, 'Mercedes', 'Alemanha', 2010),
(2, 'Ferrari', 'Itália', 1950),
(3, 'McLaren', 'Reino Unido', 1966),
(4, 'Red Bull Racing', 'Áustria', 2005),
(5, 'Racing Bulls', 'Itália', 2006),
(6, 'Alpine', 'França', 2021),
(7, 'Haas F1 Team', 'Estados Unidos', 2016),
(8, 'Audi', 'Alemanha', 2026),
(9, 'Williams', 'Reino Unido', 1977),
(10, 'Aston Martin', 'Reino Unido', 2021),
(11, 'Cadillac', 'Estados Unidos', 2026);


-- INSERINDO OS PILOTOS

INSERT INTO pilotos
(id, nome_piloto, nacionalidade, equipe_id, ano_entrou, numero_car)
VALUES
(1, 'George Russell', 'Reino Unido', 1, 2019, 63),
(2, 'Kimi Antonelli', 'Itália', 1, 2025, 12),

(3, 'Charles Leclerc', 'Mônaco', 2, 2018, 16),
(4, 'Lewis Hamilton', 'Reino Unido', 2, 2007, 44),

(5, 'Lando Norris', 'Reino Unido', 3, 2019, 1),
(6, 'Oscar Piastri', 'Austrália', 3, 2023, 81),

(7, 'Max Verstappen', 'Países Baixos', 4, 2015, 3),
(8, 'Isack Hadjar', 'França', 4, 2025, 6),

(9, 'Liam Lawson', 'Nova Zelândia', 5, 2023, 30),
(10, 'Arvid Lindblad', 'Reino Unido', 5, 2026, 41),

(11, 'Pierre Gasly', 'França', 6, 2017, 10),
(12, 'Franco Colapinto', 'Argentina', 6, 2024, 43),

(13, 'Esteban Ocon', 'França', 7, 2016, 31),
(14, 'Oliver Bearman', 'Reino Unido', 7, 2024, 87),

(15, 'Nico Hulkenberg', 'Alemanha', 8, 2010, 27),
(16, 'Gabriel Bortoleto', 'Brasil', 8, 2025, 5),

(17, 'Carlos Sainz', 'Espanha', 9, 2015, 55),
(18, 'Alexander Albon', 'Tailândia', 9, 2019, 23),

(19, 'Fernando Alonso', 'Espanha', 10, 2001, 14),
(20, 'Lance Stroll', 'Canadá', 10, 2017, 18),

(21, 'Sergio Perez', 'México', 11, 2011, 11),
(22, 'Valtteri Bottas', 'Finlândia', 11, 2013, 77),

(23, 'Yuki Tsunoda', 'Japão', 5, 2021, 22);


-- INSERINDO PAISES

INSERT INTO paises
(id, nome_pais)
VALUES
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
(14, 'Países Baixos'),
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


-- INSERINDO CIRCUITOS

INSERT INTO circuitos
(id, nome_circuito, pais_id, qtd_curvas, km)
VALUES
(1, 'Circuito Internacional do Bahrein', 1, 15, 5.412),
(2, 'Circuito Exterior do Bahrein', 1, 11, 3.543),
(3, 'Circuito Corniche de Jeddah', 2, 27, 6.174),
(4, 'Circuito de Albert Park', 3, 14, 5.278),
(5, 'Autodromo Enzo e Dino Ferrari', 4, 19, 4.909),
(6, 'Autódromo Internacional do Algarve', 5, 15, 4.653),
(7, 'Circuito de Barcelona-Catalunha', 6, 14, 4.657),
(8, 'Circuito de Mônaco', 7, 19, 3.337),
(9, 'Circuito de Baku', 8, 20, 6.003),
(10, 'Circuito Paul Ricard', 9, 15, 5.842),
(11, 'Red Bull Ring', 10, 10, 4.318),
(12, 'Silverstone Circuit', 11, 18, 5.891),
(13, 'Hungaroring', 12, 14, 4.381),
(14, 'Circuito de Spa-Francorchamps', 13, 19, 7.004),
(15, 'Circuito de Zandvoort', 14, 14, 4.259),
(16, 'Autodromo Nazionale di Monza', 4, 11, 5.793),
(17, 'Circuito de Mugello', 4, 15, 5.245),
(18, 'Autódromo de Sochi', 15, 18, 5.848),
(19, 'Nürburgring', 16, 15, 5.148),
(20, 'Istanbul Park', 17, 14, 5.338),
(21, 'Yas Marina Circuit', 18, 16, 5.281),
(22, 'Suzuka International Racing Course', 19, 18, 5.807),
(23, 'Circuito das Américas', 20, 20, 5.513),
(24, 'Autódromo Hermanos Rodríguez', 21, 17, 4.304),
(25, 'Autódromo José Carlos Pace', 22, 15, 4.309),
(26, 'Circuito Internacional de Losail', 23, 16, 5.419),
(27, 'Marina Bay Street Circuit', 24, 19, 4.940),
(28, 'Miami International Autodrome', 20, 19, 5.412),
(29, 'Las Vegas Strip Circuit', 20, 17, 6.201),
(30, 'Circuito Internacional de Xangai', 26, 16, 5.451),
(31, 'Circuito Gilles Villeneuve', 25, 14, 4.361),
(32, 'Madring', 6, 22, 5.416);


-- INSERINDO CORRIDAS 

INSERT INTO corridas
(id, data, circuito_id, pole_position_id, primeiro_lugar_id, segundo_lugar_id, terceiro_lugar_id, tempo_volta_rapida)
VALUES
(1, '2026-03-08', 4, 1, 1, 2, 3, '00:01:22.091'),
(2, '2026-03-15', 30, 2, 2, 1, 4, '00:01:35.275'),
(3, '2026-03-29', 22, 2, 2, 6, 3, '00:01:32.432'),
(4, '2026-05-03', 28, 2, 2, 5, 6, '00:01:31.869'),
(5, '2026-05-24', 31, 1, 2, 1, 3, '00:01:14.210'),
(6, '2026-06-07', 8, 2, 2, 4, 8, '00:01:13.481'),
(7, '2026-06-14', 7, 1, 4, 1, 5, '00:01:20.122'),
(8, '2026-06-28', 11, 1, 1, 2, 7, '00:01:10.374'),
(9, '2026-07-05', 12, 2, 3, 2, 5, '00:01:31.777'),
(10, '2026-07-19', 14, 2, 2, 5, 3, '00:01:48.890'),
(11, '2026-07-26', 13, 5, 5, 2, 3, '00:01:22.000'),
(12, '2026-08-23', 15, 5, 5, 2, 1, '00:01:14.230'),
(13, '2026-09-06', 16, 11, 2, 1, 7, '00:01:23.504'),
(14, '2026-09-13', 32, 5, 2, 7, 5, '00:01:35.587');


-- PONTUAÇÃO DOS PILOTOS

INSERT INTO pontuacao_pilotos
(id, corrida_id, piloto_id, colocacao, qtd_pontos)
VALUES
(1, 1, 1, 1, 25),
(2, 1, 2, 2, 18),
(3, 1, 3, 3, 15),

(4, 2, 2, 1, 25),
(5, 2, 1, 2, 18),
(6, 2, 4, 3, 15),

(7, 3, 2, 1, 25),
(8, 3, 6, 2, 18),
(9, 3, 3, 3, 15),

(10, 4, 2, 1, 25),
(11, 4, 5, 2, 18),
(12, 4, 6, 3, 15),

(13, 5, 2, 1, 25),
(14, 5, 1, 2, 18),
(15, 5, 3, 3, 15),

(16, 6, 2, 1, 25),
(17, 6, 4, 2, 18),
(18, 6, 8, 3, 15),

(19, 7, 4, 1, 25),
(20, 7, 1, 2, 18),
(21, 7, 5, 3, 15),

(22, 8, 1, 1, 25),
(23, 8, 2, 2, 18),
(24, 8, 7, 3, 15),

(25, 9, 3, 1, 25),
(26, 9, 2, 2, 18),
(27, 9, 5, 3, 15),

(28, 10, 2, 1, 25),
(29, 10, 5, 2, 18),
(30, 10, 3, 3, 15),

(31, 11, 5, 1, 25),
(32, 11, 2, 2, 18),
(33, 11, 3, 3, 15),

(34, 12, 5, 1, 25),
(35, 12, 2, 2, 18),
(36, 12, 1, 3, 15),

(37, 13, 2, 1, 25),
(38, 13, 1, 2, 18),
(39, 13, 7, 3, 15),

(40, 14, 2, 1, 25),
(41, 14, 7, 2, 18),
(42, 14, 5, 3, 15);


-- PONTUAÇÃO DAS EQUIPES

INSERT INTO pontuacao_equipes
(id, corrida_id, qtd_pontos, equipe_id)
VALUES
(1, 1, 43, 1),
(2, 1, 27, 2),

(3, 2, 43, 1),
(4, 2, 15, 2),

(5, 3, 43, 1),
(6, 3, 15, 2),

(7, 4, 40, 1),
(8, 4, 15, 2),

(9, 5, 43, 1),
(10, 5, 15, 2),

(11, 6, 43, 1),
(12, 6, 18, 2),

(13, 7, 28, 1),
(14, 7, 25, 2),

(15, 8, 43, 1),
(16, 8, 15, 4),

(17, 9, 43, 1),
(18, 9, 25, 2),

(19, 10, 43, 1),
(20, 10, 18, 3),

(21, 11, 43, 1),
(22, 11, 15, 3),

(23, 12, 43, 1),
(24, 12, 25, 3),

(25, 13, 43, 1),
(26, 13, 15, 4),

(27, 14, 35, 1),
(28, 14, 33, 3);


-- PILOTOS E EQUIPES

INSERT INTO pilotos_equipes
(id, piloto_id, equipe_id)
VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 2),
(4, 4, 2),
(5, 5, 3),
(6, 6, 3),
(7, 7, 4),
(8, 8, 4),
(9, 9, 5),
(10, 10, 5),
(11, 11, 6),
(12, 12, 6),
(13, 13, 7),
(14, 14, 7),
(15, 15, 8),
(16, 16, 8),
(17, 17, 9),
(18, 18, 9),
(19, 19, 10),
(20, 20, 10),
(21, 21, 11),
(22, 22, 11),
(23, 23, 5);


-- INSERINDO CARROS
INSERT INTO carro
(id, pilotos_id, equipe_id)
VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 2),
(4, 4, 2),
(5, 5, 3),
(6, 6, 3),
(7, 7, 4),
(8, 8, 4),
(9, 9, 5),
(10, 10, 5),
(11, 11, 6),
(12, 12, 6),
(13, 13, 7),
(14, 14, 7),
(15, 15, 8),
(16, 16, 8),
(17, 17, 9),
(18, 18, 9),
(19, 19, 10),
(20, 20, 10),
(21, 21, 11),
(22, 22, 11),
(23, 23, 5);


-- INSERINDO WC (WORLD CHAMPIONSHIP)
INSERT INTO wc
(id, piloto_id, equipe_id, carro_id, pontuacao)
VALUES
(1, 1, 1, 1, 211),
(2, 2, 1, 2, 292),
(3, 3, 2, 3, 167),
(4, 4, 2, 4, 191),
(5, 5, 3, 5, 186),
(6, 6, 3, 6, 120),
(7, 7, 4, 7, 145),
(8, 8, 4, 8, 71),
(9, 9, 5, 9, 59),
(10, 10, 5, 10, 31),
(11, 11, 6, 11, 41),
(12, 12, 6, 12, 27),
(13, 13, 7, 13, 3),
(14, 14, 7, 14, 18),
(15, 15, 8, 15, 7),
(16, 16, 8, 16, 10),
(17, 17, 9, 17, 6),
(18, 18, 9, 18, 5),
(19, 19, 10, 19, 3),
(20, 20, 10, 20, 0),
(21, 21, 11, 21, 0),
(22, 22, 11, 22, 0),
(23, 23, 5, 23, 1);


-- UPDATE

UPDATE equipes
SET nome_equipe = 'Scuderia Ferrari'
WHERE id = 2;


-- DELETE

DELETE FROM pilotos_equipes
WHERE piloto_id = 22;

DELETE FROM wc
WHERE piloto_id = 22;

DELETE FROM carro
WHERE pilotos_id = 22;

DELETE FROM pilotos
WHERE id = 22;


-- SELECT FROM

SELECT * FROM equipes;
SELECT * FROM pilotos;
SELECT * FROM paises;
SELECT * FROM circuitos;
SELECT * FROM corridas;
SELECT * FROM pontuacao_pilotos;
SELECT * FROM pontuacao_equipes;
SELECT * FROM pilotos_equipes;
SELECT * FROM carro;
SELECT * FROM wc;


-- CONSULTAS COM WHERE

-- Pilotos da equipe 1
SELECT nome_piloto
FROM pilotos
WHERE equipe_id = 1;

-- Pilotos da equipe 2
SELECT nome_piloto
FROM pilotos
WHERE equipe_id = 2;

-- Pilotos que entraram na Fórmula 1 em 2025
SELECT nome_piloto
FROM pilotos
WHERE ano_entrou = 2025;

-- Pilotos de uma determinada nacionalidade
SELECT nome_piloto
FROM pilotos
WHERE nacionalidade = 'Brasil';
