#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kod_morsa.py
#  


kod = {'a': '+-', 'ą':'+-+-', 'b': '-+++', 'c': '-+-+', 'ć': '-+-++',
    'd': '-++', 'ę': '++-++', 'f': '++-+', 'g': '--+', 'h': '++++',
    'i': '++', 'j': '+---', 'k': '-+-', 'l':'+-++', 'ł': '+-++-',
    'm': '--','n': '-+', 'ń': '--+--', 'o': '---', 'p': '+--+', 'q': '--+-',
    'r': '+-+', 's': '+++', 'ś': '+++-+++', 't': '-', 'u': '++-',
    'v': '+++-', 'w': '+--', 'x':'-++-', 'y': '-+--', 'z':'--++',
    'ż': '--+-+', 'ź':'--++-', ' ': ' '}

def koduj():    
    t = input('Podaj tekst: ').lower()
    print("".join([kod[l] for l in t]))


def dekoduj():
    t = []
    l = ' '
    while l > '':
        l =input("Podaj kod morse'a': ")
        t.append(l)
    print(t)

def main(args):
    dekoduj()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
