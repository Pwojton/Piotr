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
    int i;
    for (i=0; i<st; i++) {
        cout << tb[i] << "x^" << st-i << " + ";
    }
    cout << tb[i] << endl;
}
//horner_re(2,3, tbwsp)
//horner_re(2,3, tbwsp) * 2+4
//horner_re(2,3, tbwsp) * 2+5
//horner_re(2,3, tbwsp) * 2+3
//2
//2 * 2 + 3 = 7
//7*2 + 3 = 19
//19 * 2 + 4 = 42
//42
//

float horner_re(float x, int stopien, float tbwsp[])
{
    if (stopien == 0)
        return tbwsp[0];
    return horner_re(x, stopien-1, tbwsp) * x + tbwsp[stopien];
}

float horner_it(float x, int stopien, float tbwsp[])
{
    float wynik = tbwsp[0];

    for(int i =0; i <= stopien; i++)
        wynik = wynik * x + tbwsp[i];
    
    return wynik;
}

int main(int argc, char **argv)
{
    int stopien = 0;
    float *tbwsp; //wskażnik - zmienna zawierająca adres komórki
    float x =0; //argument
	cout << "Stopień wielomianu: ";
    cin >> stopien;

    tbwsp = new float [stopien+1];
    //cout << tbwsp; - wyswietanie wskaznika

    for(int i=0; i <= stopien; i++) {
        cout << "podaj wsopółczynnik przy potędze " << stopien-i << ": ";
        cin >> tbwsp[i];
    }

    cout << "Argument: ";
    cin >> x;

    cout << "Wartość wielomianu o postaci: ";
    drukujw(stopien, tbwsp);
    cout << "wynosi: " << horner_it(x, stopien, tbwsp) << endl;
    cout << "wynosi: " << horner_re(x, stopien, tbwsp) << endl;
    
    
	return 0;
}
