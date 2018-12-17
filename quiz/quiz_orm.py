#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from modele import *
from baza import czy_jest, dane_z_pliku


# ~def dodaj_dane(dane):

    # ~for model, plik in dane.items():
        # ~pola = [pole for pole in model._meta.fields]
        # ~pola.pop(0)
        # ~wpisy = dane_z_pliku(plik + '.csv')
        # ~with baza.atomic():
            # ~model.insert_many(wpisy, fields=pola).execute()


def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()
    baza.create_tables([Kategoria, Pytanie, Odpowiedz])

    # ~dane = {
        # ~Klasa: 'klasy',
        # ~Uczen: 'uczniowie',
        # ~Ocena: 'oceny',
        # ~Przedmiot: 'przedmioty',
    # ~}

    # ~dodaj_dane(dane)

    baza.close()
    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
