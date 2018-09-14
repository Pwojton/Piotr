#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  abc.py
#Program pobiera 3 liczby całkowite i wyświetla liczbę największą

def maks(a, b ,c):
    maks = a
    
    if b > maks:
        maks = b
    if c > maks:
        maks =c
    return maks
    
def main(args):
   # a = int(input('Podaj 1 liczbę: '))
   # print(a)
   # b = int(input('Podaj 2 liczbę: '))
   # print(b)
   # c = int(input('Podaj 3 liczbę: '))
   # print(b)
    assert(maks(3, 2, 1), == 3)
    assert(maks(2, 2, 1), == 3)
    assert(maks(1, 2, 3), == 3)
    assert(maks(1, 1, 3), == 3)
    assert(maks(3, 1, 1), == 3)
    assert(maks(3, 3, 1), == 3)
    assert(maks(3, 3, 3), == 3)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
