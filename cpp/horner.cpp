/*
 * horner.cpp
 * w(x) = 2x^3 + 3x^2 + 5x + 4 => 6
 * w(x) = x (2x^2 + 3x + 5) + 4
 * w(x) = x (x (2x+ 3) + 5) + 4 => 3
 */


#include <iostream>
using namespace std;

void drukujw(int st, float tb[])
{
    for (int i=st; i>=0; i-- ) {
        cout <<"x"<< "^"<<tb[i];
    }
    cout <<"+"<< tb[st];
        
}

int main(int argc, char **argv)
{
    int stopien = 0;
    float *tbwsp; //wskażnik - zmienna zawierająca adres komórki
    float x =0; //argument
	cout << "Stopień wielomianu: ";
    cin >> stopien;

    tbwsp = new float [stopien+1];
    cout << tbwsp;

    for(int i=0; i <= stopien; i++) {
        cout << "podaj wsopółczynnik przy potędze " << stopien-i << ": ";
        cin >> tbwsp[i];
    }

    cout << "Argument: ";
    cin >> x;

    cout << "Wartość wielomianu o postaci: ";
    drukujw(stopien, tbwsp);
    
    
	return 0;
}

