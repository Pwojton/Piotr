#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  sonce.py

import turtle as t

def figura(bok, kat, ile):
    
    for i in range(ile):
        t.forward(bok)
        t.right(kat)
        
def figura_rek(bok, kat, ile, krok):
    t.forward(bok)
    t.right(kat)
    if ile > 0: # warunek brzegowy
        figura_rek(bok - krok, kat + krok, ile - 1, krok)


def main():
    t.setup(800, 600)
    t.color('blue', 'red')
    t.begin_fill()
    t.speed(0)

    figura_rek(200, 15, 500, 5)

    t.end_fill()
    t.done()
    return 0

main()
