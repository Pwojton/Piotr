#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma-cyfr.py
#  
#  Copyright 2018  <>
#  
#  


def sumuj_cyfry1(a):
    suma = 0
    while a > 0:
        suma += a % 10
        a = int(a / 10)
    return suma
    
def sumuj_cyfry2(a):
    

def main(args):
    a = int(input("Podaj liczbę: "))
    a = int(a)
    suma = 0
    
    while a < 10:
        a = int(input("Podaj liczbę 2-cyfrową: "))
        a = int(a)
        
    while a > 0:
        suma += a % 10
        a = int(a / 10)
        
    print("Suma:", suma)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(sumuj_cyfre1(sys.argv))
