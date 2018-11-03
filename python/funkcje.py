#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  szablon.py

#Zasięg zmiennych może być lokalny lub globalny

def dodaj(a, b):
    return(a + b)
    
def odejmij(a, b):
    return(a - b)
       
def pomnoz(a, b):
    return(a * b)
    
def podziel(a, b):
    return(a / b)
        
def main(args):
    
    a = int(input('Podaj 1 liczbę: '))
    print(a)
    b = int(input('Podaj 2 liczbę: '))
    print(b)
    
    print("Suma: ", dodaj(a, b)) 
    print("Różńica: ",odejmij(a, b) ) 
    print("Iloraz: ", pomnoz(a, b)) 
    print("Iloczyn: ", podziel(a, b)) 
    
    return 0
    
# duck typing

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
