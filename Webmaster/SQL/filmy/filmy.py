#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv


def dane_z_pliku(nazwa_pliku):
    dane = []  # pusta lista na dane
    with open(nazwa_pliku, newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter='\t')
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]  # usuwanie zbędnych spacji
            dane.append(rekord)
    return dane


def kwerenda1(cur):
    cur.execute("""
        SELECT name, rating
        FROM filmy
        WHERE genre = 'romance' AND year BETWEEN 1990 AND 1999
        ORDER BY rating
        DESC LIMIT 2, 3;
    """)

    wyniki = cur.fetchall()
    for rekord in wyniki:
        print(rekord)


def main(args):
    con = sqlite3.connect('filmy.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    with open('filmy.sql', 'r') as plik:
        cur.executescript(plik.read())

    filmy = dane_z_pliku('filmy.txt')
    filmy.pop(0)  # usunięcie pierwszego elementu listy
    cur.executemany('INSERT INTO filmy VALUES(?, ?, ?, ?, ?)', filmy)

    kwerenda1(cur)

    con.commit()  # zatwierdzenie wszystkich informacji w bazie
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
