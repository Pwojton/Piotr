#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    liczba = random.randint(1, 10)
    # print("Wylosowano:", liczba)
    # pobieranie danych od użytkownika
    for i in range(3):
        print("Próba", i + 1)
        odp = input("Podaj liczbę od 1 do 10")  # losowanie liczby
        print("Podałeś liczbe:", odp)

        if liczba == int(odp):  # porównanie odp z wylosowaną liczbą
            print("Zgadłeś!")
            break  # przerwaniedziałania pętli
        elif i == 2:
            print("Wylosowano:", liczba)
        else:
            print("Spróbuj innym razem!")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
