#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py
#  

def trojkat(a, b, c):
    """
    Funkcja bada możliwość zbudowania trójkąta z trzech podanych boków
    Funkcja zwraca True jeżeli się da, False w przeciwnym wypadku
    """
    if a + b > c and b + c > a and a + c > b:
        return True
        
    return False

def main(args):
    assert(trojkat(3, 4, 5) == True)
    assert(trojkat(3, 4, 1) == False)
    
    # a = int(input('Podaj 1 krótszy bok: '))
    # print(a)
    # b = int(input('Podaj 2 krótszy bok: '))
    # print(b)
    # c = int(input('Podaj najdłuższy bok: '))
    # print(a)
    
    # ~if trojkat(a, b, c):
        # ~print("Da się")
    # ~else:
        # ~print("Nie da rady")
        
    print(trojkat(a, b, c))

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
