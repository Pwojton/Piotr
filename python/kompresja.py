#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  


def main(args):

    Vk = 747171
    Vnk = 117760
    Rc = int(Vk) / int(Vnk) * 100
    R2c = (1 - int(Vk) / int(Vnk)) * 100  
    print('Współczynnik kompresji: ', Rc)
    print('Ile miejsca zaoczczędzono: ', R2c)

    Vk2 = 70074
    Vnk2 = 117760
    Rc2 = int(Vk2) / int(Vnk2) * 100
    R2c2 = (1 - int(Vk2) / int(Vnk2)) * 100  
    print('Współczynnik kompresji: ', Rc2)
    print('Ile miejsca zaoczczędzono: ', Rc22)


    
    return 0
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
