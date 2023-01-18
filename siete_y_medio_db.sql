CREATE DATABASE siete_y_medio_db CHARACTER SET utf8mb4;
USE siete_y_medio_db;

/*Creacion de las tablas*/
CREATE TABLE player (
    player_id VARCHAR(25) PRIMARY KEY,
    player_name VARCHAR(40) NOT NULL,
    player_risk TINYINT NOT NULL,
    human TINYINT NOT NULL
);

CREATE TABLE deck (
	deck_id CHAR(3) PRIMARY KEY ,
    deck_name VARCHAR(25)
);

CREATE TABLE cardgame (
	cardgame_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	players TINYINT NOT NULL,
    rounds TINYINT NOT NULL,
    start_hour DATETIME NOT NULL,
    end_hour DATETIME NOT NULL,
    deck_id CHAR(3) NOT NULL,
    FOREIGN KEY (deck_id) REFERENCES deck(deck_id)
);

CREATE TABLE card (
	card_id CHAR(3) PRIMARY KEY,
    card_name VARCHAR(25) NOT NULL,
    card_value DECIMAL(3,1) NOT NULL,
    card_priority TINYINT NOT NULL,
    card_real_value TINYINT NOT NULL,
    deck_id CHAR(3) NOT NULL,
    FOREIGN KEY (deck_id) REFERENCES deck(deck_id)
);

CREATE TABLE player_game_round (
	cardgame_id INT UNSIGNED,
	FOREIGN KEY (cardgame_id) REFERENCES cardgame(cardgame_id),
    round_num INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    player_id VARCHAR(25),
    FOREIGN KEY (player_id) REFERENCES player(player_id),
    is_bank TINYINT(1) NOT NULL,
    bet_points TINYINT,
    cards_value DECIMAL(4,1) NOT NULL,
    starting_round_points TINYINT,
    ending_round_points TINYINT
);

CREATE TABLE player_game (
	cardgame_id INT UNSIGNED,
	FOREIGN KEY (cardgame_id) REFERENCES cardgame(cardgame_id),
    player_id VARCHAR(25),
    FOREIGN KEY (player_id) REFERENCES player(player_id),
    initialcard_id CHAR(3) NOT NULL,
    starting_points TINYINT NOT NULL,
    ending_points TINYINT NOT NULL  
);

/*Creacion de las vistas*/
CREATE VIEW profits as
select ending_points-starting_points as profit
from player_game;

CREATE VIEW games_played as
select count(player_id) as games_played
from player_game;

CREATE VIEW minutes_played as
select (TIMEDIFF(end_hour,start_hour)) as minutes_played
from cardgame
where cardgame_id in (select cardgame_id from player_game);

/*Insert Baraja española*/
INSERT INTO deck VALUES("esp", "Spanish Deck");
/*Insert cartas de Baraja española*/
/* OROS */
INSERT INTO card VALUES("O01", "AS de Oros", 1, 4, 1, "esp");
INSERT INTO card VALUES("O02", "Dos de Oros", 2, 4, 2, "esp");
INSERT INTO card VALUES("O03", "Tres de Oros", 3, 4, 3, "esp");
INSERT INTO card VALUES("O04", "Cuatro de Oros", 4, 4, 4, "esp");
INSERT INTO card VALUES("O05", "Cinco de Oros", 5, 4, 5, "esp");
INSERT INTO card VALUES("O06", "Seis de Oros", 6, 4, 6, "esp");
INSERT INTO card VALUES("O07", "Siete de Oros", 7, 4, 7, "esp");
INSERT INTO card VALUES("O10", "Sota de Oros", 0.5, 4, 10, "esp");
INSERT INTO card VALUES("O11", "Caballo de Oros", 0.5, 4, 11, "esp");
INSERT INTO card VALUES("O12", "Rei de Oros", 0.5, 4, 12, "esp");

/* COPAS */
INSERT INTO card VALUES("C01", "AS de Copas", 1, 3, 1, "esp");
INSERT INTO card VALUES("C02", "Dos de Copas", 2, 3, 2, "esp");
INSERT INTO card VALUES("C03", "Tres de Copas", 3, 3, 3, "esp");
INSERT INTO card VALUES("C04", "Cuatro de Copas", 4, 3, 4, "esp");
INSERT INTO card VALUES("C05", "Cinco de Copas", 5, 3, 5, "esp");
INSERT INTO card VALUES("C06", "Seis de Copas", 6, 3, 6, "esp");
INSERT INTO card VALUES("C07", "Siete de Copas", 7, 3, 7, "esp");
INSERT INTO card VALUES("C10", "Sota de Copas", 0.5, 3, 10, "esp");
INSERT INTO card VALUES("C11", "Caballo de Copas", 0.5, 3, 11, "esp");
INSERT INTO card VALUES("C12", "Rei de Copas", 0.5, 3, 12, "esp");

/* ESPADAS */
INSERT INTO card VALUES("E01", "AS de Espadas", 1, 2, 1, "esp");
INSERT INTO card VALUES("E02", "Dos de Espadas", 2, 2, 2, "esp");
INSERT INTO card VALUES("E03", "Tres de Espadas", 3, 2, 3, "esp");
INSERT INTO card VALUES("E04", "Cuatro de Espadas", 4, 2, 4, "esp");
INSERT INTO card VALUES("E05", "Cinco de Espadas", 5, 2, 5, "esp");
INSERT INTO card VALUES("E06", "Seis de Espadas", 6, 2, 6, "esp");
INSERT INTO card VALUES("E07", "Siete de Espadas", 7, 2, 7, "esp");
INSERT INTO card VALUES("E10", "Sota de Espadas", 0.5, 2, 10, "esp");
INSERT INTO card VALUES("E11", "Caballo de Espadas", 0.5, 2, 11, "esp");
INSERT INTO card VALUES("E12", "Rei de Espadas", 0.5, 2, 12, "esp");

/* BASTOS */
INSERT INTO card VALUES("B01", "AS de Bastos", 1, 1, 1, "esp");
INSERT INTO card VALUES("B02", "Dos de Bastos", 2, 1, 2, "esp");
INSERT INTO card VALUES("B03", "Tres de Bastos", 3, 1, 3, "esp");
INSERT INTO card VALUES("B04", "Cuatro de Bastos", 4, 1, 4, "esp");
INSERT INTO card VALUES("B05", "Cinco de Bastos", 5, 1, 5, "esp");
INSERT INTO card VALUES("B06", "Seis de Bastos", 6, 1, 6, "esp");
INSERT INTO card VALUES("B07", "Siete de Bastos", 7, 1, 7, "esp");
INSERT INTO card VALUES("B10", "Sota de Bastos", 0.5, 1, 10, "esp");
INSERT INTO card VALUES("B11", "Caballo de Bastos", 0.5, 1,11, "esp");
INSERT INTO card VALUES("B12", "Rei de Bastos", 0.5, 1, 12, "esp");
