#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  warunki.py



def main(args):
    a = int(input('Podaj 1 liczbę: '))
    print(a)
    b = int(input('Podaj 2 liczbę: '))
    print(b)
    
    if a > b:  # początke funkcji warunkowej
        print(a, "jest większe od", b)
    elif b > a:  
        print(b, "jest większe od", a)
    else a == b: 
        print(a, "równa się", b)

    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
