/*
 * silnia.cpp
 */


#include <iostream>
using namespace std;

int silnia_it(int n) {
    int wynik = 1;

    for(int i = 1; i <= n; i++) {
        wynik = wynik * i;
    }
    return wynik;
}

int silnia_rek(int n)
{
    int wynik = 1;

    if (n < 2)
        return 1;
    else
        return silnia_rek(n - 1) * n;
    return wynik;
    
}

int main(int argc, char **argv)
{
	int n;
    cout << "Podaj liczbę: ";
    cin >> n;
    cout << "Silnia liczby " << n << " wynosi: " << silnia_it(n) << endl;
    cout << "Silnia liczby " << n << " wynosi: " << silnia_rek(n);
    //cout << "Silnia liczby " << n << "wynosi" << silnia_rek(n);

    
	return 0;
}

