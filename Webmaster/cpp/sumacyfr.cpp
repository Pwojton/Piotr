/*
 * sumacyfr.cpp
 */


#include <iostream>
using namespace std;

int sumuj_cyfry1(int liczba)
{
    int suma = 0;
    
    while(liczba > 0)
    {
        suma += liczba % 10;
        liczba = liczba / 10;
    }
    return suma;
}

int main(int argc, char **argv)
{
    int liczba;
    liczba = 0;
    while(liczba < 10)
        {
            cout << "Podaj min liczbę 2-cyfrową: "; //stały napis
            cin >> liczba;  //podaj a
        } 
    
    cout << "Suma: " << sumuj_cyfry1(liczba) << endl;
    
	return 0;
}

