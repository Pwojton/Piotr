#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
# Program drukuj wypełniony prostokąt o bokach podanych przez użytkownika 
 
def prostokat1(a, b):
    for i in range(a):
        for j in range(b):
            print("#", end='')
        print()
 
 
def prostokat2(a, b, c):
    for i in range(a):
        if i == 0 and i == b:
            print("#", end='')
        for j in range(b):
            if j == 0 or j == b -1:
                print("#", end='')
            else:
                print(" ", end=' ')
        print()

    

def main(args):
    a = int(input('Podaj szerokość prostokąta: '))
    b = int(input('Podaj długość prostokąta: '))
    c = int(input('Podaj wypełnienie prostokąta: '))
    
    print(prostokat2(a, b, c))

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
