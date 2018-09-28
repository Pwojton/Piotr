#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cw2.py
#
#DANE WEJŚCIOWE:
# liczby dodatnie podawane przez użytkownika
#DANE WYJŚCIOWE:
#suma liczb podanych przez użytkownika 
#program musi zapewnić poprawnośc danych
#program kończy działanie po wprowadzeniu wartości 0
#



def main(args):
    
    suma = 0
    liczba = -1 
    
    while liczba != 0:
        liczba  = int(input("Podaj liczbę: "))
        while liczba < 0:  # pętla zaporowa - pętla która wymusza wprowadzemie poprawnych danych
            liczba  = int(input("Błedne dane! Podaj liczbę: "))
        suma += liczba
        
    print("Suma: ", suma)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
