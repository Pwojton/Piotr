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

// silnia_re(5) 
// silnia_re(4) * 5
// silnia_re(3) * 4
// silnia_re(2) * 3
// silnia_re(1) * 2
// silnia_re(0) * 1
// 1
// 1*1
// 1*2
// 2*3
// 6*4
// 24*5
// 120

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

