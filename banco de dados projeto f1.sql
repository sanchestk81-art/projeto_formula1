-- 1. CRIAÇÃO DAS TABELAS

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


-- 2. CHAVES ESTRANGEIRAS

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


-- 3. INSERINDO AS EQUIPES

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


-- 4. INSERINDO OS PILOTOS

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
(22, 'Valtteri Bottas', 'Finlândia', 11, 2013, 77);


-- 5. UPDATE

UPDATE equipes
SET nome_equipe = 'Scuderia Ferrari'
WHERE id = 2;


-- 6. DELETE

DELETE FROM pilotos
WHERE id = 22;


-- 7. SELECT FROM

SELECT * FROM paises;

SELECT * FROM equipes;

SELECT * FROM pilotos;

SELECT * FROM circuitos;

SELECT * FROM corridas;

SELECT * FROM pontuacao_pilotos;

SELECT * FROM pontuacao_equipes;

SELECT * FROM pilotos_equipes;

SELECT * FROM carro;

SELECT * FROM wc;


-- 8. CONSULTAS COM WHERE

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