DROP TABLE IF EXISTS miasta;
DROP TABLE IF EXISTS mieszkancy;
DROP TABLE IF EXISTS powierzchnie;

CREATE TABLE miasta (
	id_miasta INTEGER PRIMARY KEY AUTOINCREMENT,
	nazwa_miasta TEXT,
	wojewodztwo TEXT
);

CREATE TABLE mieszkancy (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    liczba_mieszkancy INTEGER,
    liczba_kobiet INTEGER,
    grupa_wiekowa TEXT(20),
    data_aktulizacji DATE,
    id_miasta INTEGER,
    FOREIGN KEY (id_miasta) REFERENCES mieszkancy(id)
);

CREATE TABLE powierzchnie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    powierzchnia DECIMAL,
    powierzchnia_terenów_zielonych INTEGER,
    data_aktulizacji DATE,
    id_miasta INTEGER,
    FOREIGN KEY (id_miasta) REFERENCES powierzchnie(id)
);