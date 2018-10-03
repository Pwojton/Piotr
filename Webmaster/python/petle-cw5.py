
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pentle_cw_2.py





def main(args):
    
    suma = 0
    liczba = 1
    
    while liczba != 0:
        liczba = int(input("Podaj liczbę: "))
        while liczba < 0:  # pętla zaporowa
            liczba = int(input("Błędne dane! Wprowadzane liczby powinny być dodatnie. Podaj liczbę jeszcze raz: "))
        suma += liczba
    print("suma: ", suma)
    return 0
    
def main2(args):
    
    suma = 0
    liczba = 1
    
    while liczba != 0:
        liczba = int(input("Podaj liczbę: "))
        if liczba < 0:
            print("Błędne dane! ", end='')
        else:
            suma += liczba
    print("suma: ", suma)
    return 0

def main3(args):
	
	nazwa = ['','styczeń','luty','marzec','kwiecień','maj','czerwiec','lipiec','sierpień','wrzesień','paździenik','listopad','grudzień']
	
	a = 3
	
	while a > 0:
		a = a - 1
		miesiac = int(input("podaj numer miesiąca: "))
		if miesiac > 12 or miesiac < 1:
			print("Błędne dane! Wpisz raz: ")
		else:
			print (nazwa[miesiac])
	return 0

def main4(args):
	suma = 0
	liczby = []
	a = int(input("Podaj liczbę: "))
	
	liczby = list(map(int, str(a)))

	print (sum(liczby))
	return 0

if __name__ == '__main__':
    import sys
sys.exit(main3(sys.argv))
