/*
 * sito_eratostenesa.cpp
 */


#include <iostream>
#include <cmath>
using namespace std;

int main(int argc, char **argv)
{
    int i, j, zakres, b;
    bool tablica[100];
    cout << "Podaj górny zakres, max 99: " << endl;
    cin >> zakres;
    b = sqrt((float)zakres);
    cout << b;

    //inicjacja tablicy
    for (i=2; i < zakres + 1; i++)
        tablica[i] = true;
    for (i=2; i <= b; i++) {
        if (tablica[i] != false)
            for (j = i+i; j < zakres + 1; j+=i)
                tablica[j] = false;
    }
    
    for (i = 2; i < zakres+1; i++) {
        if(tablica[i] == true)
        cout << i << endl;
    }
	return 0;
}

