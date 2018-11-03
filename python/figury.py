#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
#  
def prostokat(a, b, c):
    
    for i in range (a):
        for j in range (b):
            print(c, end ='')
        print()

def prostokat_2(a, b, c):

    for i in range (a):
        for j in range (b):
            if j == 0 or  j == b - 1 or i == 0 or i == a - 1:
                print(c, end ='')
            else:
                print(" ", end = '')
        print()
        
def choinka(h, c):
    
    for i in range (h):
        for j in range (i + 1):
            print(c, end = '')
        print ()

def choinka_2(h, c):
    
    for i in range (h):
        for j in range (h - i):
            print(c, end = '')
        print ()
        
def trojkat (h):
    m = (h-1)*2
    for i in range(h-1, -1, -1):
        for j in range(m+1):
            if j < i or j > m-i:
                print(" ", end='')
            else:
                print("$", end='')
        print()

def main(args):
#    a = int(input("Wysokość prostokąta:"))
#    b = int(input("Długość prostokąta:"))
    h = int(input("Wysokość trójkąta:"))
#    c = input("podaj znkak wypenienia: ")
    
    print(trojkat(h))
    
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
