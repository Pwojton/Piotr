/*
 * szabloncpp.cpp
 */


#include <iostream>     

using namespace std; //domyślną biblioteką jest standardowa

int dodaj(int a, int b)
{
    return a+b;
}

int odejmij(int a, int b)
{
    return a - b;
}

int pomnoz(int a, int b)
{
    return a*b;
}

float podziel(float a, float b)
{
    return a/b;
}

int main(int argc, char **argv)
{
	float a, b; //typ zmiennej który pzryjmuje wratości z rozwinięciem dziesiętnym 
    a = b = 0;
    
    cout << "Podaj 1. liczbę: "; //stały napis
    cin >> a;  //podaj a
    cout << a << endl;  //zwróć a
    
    cout << "Podaj 2. liczbę: "; //stały napis
    cin >> b;  //podaj b
    cout << b << endl;  //zwróć b
   
    dodaj(5, 6);
    
    cout<< "Suma: " << dodaj(a, b) << endl; //doadaj a i b
    cout<< "Iloczyn: " << odejmij(a, b) << endl; //odejmij a i b
    cout<< "Róznica: " << pomnoz(a, b) << endl; //podziel a i b
    cout<< "Iloraz: " << podziel(a, b) << endl; //pomnóż a i b
    
	return 0;
}

