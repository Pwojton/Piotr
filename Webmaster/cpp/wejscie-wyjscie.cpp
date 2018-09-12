/*
 * szabloncpp.cpp
 */


#include <iostream>     

using namespace std; //domyślną biblioteką jest standardowa

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
    
    cout<< "Suma: " << a + b << endl; //doadaj a i b
    cout<< "Iloczyn: " << a / b << endl; //odejmij a i b
    cout<< "Róznica: " << a - b << endl; //podziel a i b
    cout<< "Iloraz: " << a * b << endl; //pomnóż a i b
    
	return 0;
}

