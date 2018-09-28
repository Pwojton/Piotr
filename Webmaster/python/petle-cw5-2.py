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


def pobierzMiesiac():
    
    nazwy = ['', 'styczeń', 'luty', 'marzec', 'kwiecien']
    
    miesiac = 9
    a = int(input("Podaj numer miesiąca: "))
    
    if a > 0 and a < 12:
        for a in range(3):
            
    # Napisz program który sumuje cyfry liczby pdanej przez użytkownika. 



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


def main2(args):
    
    suma = 0
    liczba = -1 
    
    while liczba != 0:
        liczba  = int(input("Podaj liczbę: "))
        if liczba < 0:  # pętla zaporowa - pętla która wymusza wprowadzemie poprawnych danych
            print("Błedne dane!", end='')
        else:
            suma += liczba
        
    print("Suma: ", suma)
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(pobierzMiesiac(sys.argv))
