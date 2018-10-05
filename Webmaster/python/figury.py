#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  figury.py
# Program drukuj wypełniony prostokąt o bokach podanych przez użytkownika 
 
def prostokat1(a, b):
    for i in range(a):
        for j in range(b):
            print("#", end='')
        print()
 
 
def prostokat2(a, b):
    """ Drukowanie pustego prostokąta """
    for i in range(a):
        for j in range(b):
            if j == 0 or j == b -1 or i == 0 or i == a -1:
                print("#", end='')
            else:
                print(" ", end=' ')
        print()

def choinka(h):
    """ Drukowanie choinki """
    for i in range(6):
        for j in range(h + 1):
            print("$", end='')
        print()
                        
    
def trojkat(h, p):
    """ Drukowanie trójkąta """
    for i in range(6):
        for j in range(7):
            print("$", end='')

def main(args):
    #a = int(input('Podaj DŁUGOŚĆ prostokąta: '))
    #h = int(input('Podaj wysokość prostokąta: '))
    #z = "z"
    h = 6
    p = 8
    
    choinka(h)


if __name__ == '__main__':
    import sys
    sys.exit(trojkat(sys.argv))
