#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    ileliczb = int(input("Ile liczb wytypujesz?"))
    maksliczba = int(input("Podaj maks losowaną liczbe"))
    print("Wytypuj {} z {} liczb: ".format(ileliczb, maksliczba))

    liczby = []  # definicja psutej listy na losowanie liczby
    i = 0  # licznik uniklanych Wylosowanych liczb
    # for i in range(ileliczb):
    while i < ileliczb:
        liczba = random.randint(1, maksliczba)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i += 1  # powiększ licznik o1
    print("Wylosowano: ", liczby)

    typy = set()  # def. pustego zbioru na typy
    i = 0  # licznik unikalnych typow użytkownika
    while i < ileliczb:
        typ = input("Podaj liczbę {}: ".format(i + 1))
        if typ not in typy:
            typy.add(typ)
            i += 1  # powiększ licznik o 1
    print("Wytypowane: ", typy)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
