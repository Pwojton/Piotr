DROP TABLE IF EXISTS uczniowie;
DROP TABLE IF EXISTS klasy;
DROP TABLE IF EXISTS przedmioty;
DROP TABLE IF EXISTS oceny;

CREATE TABLE uczniowie (
id INTEGER PRIMARY KEY,
imie TEXT,
nazwisko TEXT,
plec INTEGER
id_klasa INTEGER,
egz_hum NUMERIC,
egz_mat NUMERIC,
egz_jez NUMERIC
);

CREATE TABLE klasy (
id INTEGER PRIMARY KEY AUTOINCREMENT,
klasa TEXT(2),
rok_naboru INTEGER(4),
rok_matury INTEGER(4)
);

CREATE TABLE przedmioty (
id INTEGER PRIMARY KEY AUTOINCREMENT,
przedmiot TEXT,
imie_naucz TEXT,
nazwisko_naucz TEXT,
plec_naucz INTEGER(1)
);

CREATE TABLE oceny (
id INTEGER PRIMARY KEY AUTOINCREMENT,
data DATE,
ocena INTEGER(1),
id_uczen INTEGER,
id_przedmiot INTEGER,
FOREIGN KEY (id_uczen) REFERENCES uczniowie(id),
FOREIGN KEY (id_przedmiot) REFERENCES przedmioty(id)
);
