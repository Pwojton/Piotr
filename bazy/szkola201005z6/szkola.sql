DROP TABLE IF EXISTS uczniowie;
DROP TABLE IF EXISTS przedmioty;
DROP TABLE IF EXISTS oceny;

CREATE TABLE uczniowie (
	id_uczen INTEGER PRIMARY KEY AUTOINCREMENT,
	nazwiska TEXT,
	imie TEXT,
	ulica TEXT,
	dom INTEGER,
	id_klasy TEXT
);

CREATE TABLE przedmioty (
	id_przedmiot INTEGER PRIMARY KEY,
	przedmiot TEXT,
	nazwisko_naucz TEXT,
	imie_naucz TEXT,
	FOREIGN KEY (id_przedmiot) REFERENCES id(przedmiot)
);

CREATE TABLE oceny (
	id_uczen INTEGER,
	ocena INTEGER(1),
	data DATE,
	id_przedmiot INTEGER,
	FOREIGN KEY (id_uczen) REFERENCES id(uczen),
	FOREIGN KEY (id_przedmiot) REFERENCES id(przedmiot)
);
