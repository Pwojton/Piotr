#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla-for.py
#  


def main(args):
    a = int(input('Podaj 1 liczbę: '))
    b = int(input('Podaj 2 liczbę: '))   
    
    while a >= b:
        a = int(input('Podaj 1 liczbę: '))
        b = int(input('Podaj 2 liczbę: '))
         
    if a >= b:
        print("Błędny zakres")
        
    for liczba in range(a, b + 1):
        if liczba % 2 == 0:
            print(liczba)        
      
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
