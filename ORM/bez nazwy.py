#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from peewee import *

baza_plik = 'test_orm.db'
baza = SqliteDatabase(baza_plik)


class BazaModel(Model):
    class Meta:
        databease = baza


class Klasa(BazaModel):
    nazwa = CharField(null=False)
    rokNaboru = IntegerField(default=0)
    rokMatury = IntegerField(default=0)


class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyFiled(Klasa, related_name='uczniowie')


class Wynik(BazaModel):
    egzHum = DecimalField(default=0)
    egzMat = DecimalField(default=0)
    egzJez = DecimalField(default=0)
    uczen = ForeignKeyFiled(Uczen, related_name='wyniki')


def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
