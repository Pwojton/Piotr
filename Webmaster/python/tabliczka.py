#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tabliczka.py
#  
#  Copyright 2018  <>
#  Program drukuje tabliczke mnożenia do 10
#   pyformat.com

def tabliczka():
    for i in range(1, 11):# ilość wierszy
        print(" ")
        for j in range(1, 11): # ilość kolumn
            print('{:>3} '.format(i * j), end=' ')

def main(args):
   # a = int(input("Podaj pierwszą liczbe: "))
   # b = int(input("Podaj pierwszą liczbe: "))
    
    tabliczka()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
