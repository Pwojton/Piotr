#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py
import sqlite3

def kwerenda(cur):
    cur.execute("""
        WITH srednie AS (
        SELECT imie, nazwisko, AVG(ocena) AS sred FROM uczniowie
        INNER JOIN  oceny ON  uczniowie.id=oceny.id_uczen
        GROUP BY uczniowie.id
    ) SELECT nazwisko, imie, sred FROM srednie
    WHERE sred > 3.5 ORDER BY sred DESC
    """)
    
    # % - dowolny ciąg znaków 
    #
    # SELECT COUNT(*) FROM uczniowie WHERE plec=0
    # SELECT id FROM uczniowie WHERE imie='Anna' AND nazwisko="Ignaczuk"
    # SELECT COUNT(*) FROM uczniowie WHERE imie LIKE '%a'- liczba dziewczyn w tablei
    # ORDER BY nazwisko DESC|ASC
    # SELECT AVG(egz_mat), AVG(egz_jez), AVG(egz_hum) FROM uczniowie 
    # SELECT MAX(egz_mat), MIN(egz_jez), MIN(egz_hum) FROM uczniowie
    # SELECT imie, nazwisko, klasa FROM uczniowie INNER JOIN klasy ON uczniowie.id_klasa=klasy.id
    # SELECT imie, nazwisko, klasa FROM uczniowie INNER JOIN klasy ON uczniowie.id_klasa=klasy.id WHERE klasa='1A' AND rok_naboru=2012
    #
    #    WITH srednie AS (
    #    SELECT imie, nazwisko, AVG(ocena) AS sred FROM uczniowie
    #    INNER JOIN  oceny ON  uczniowie.id=oceny.id_uczen
    #    GROUP BY uczniowie.id
    #   ) SELECT nazwisko, imie, sred FROM srednie
    #   WHERE sred > 3.5 ORDER BY sred DESC
    #
    #
    #
    # Typy relacji:
    # 1. Jeden do wielu
    # 2. Jeden do wielu
    # 3. Wiele do wielu
    #
    
    wyniki = cur.fetchall()
    for row in wyniki:
        print(row)
    
def main(args):
    # KONFIGURACJA #####
    baza_nazwa = 'uczniowie'
    tabele = ['uczniowie', 'klasy', 'przedmioty', 'oceny']
    
    con = sqlite3.connect(baza_nazwa + '.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora
    
    kwerenda(cur)
    
    con.commit()
    con.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
