/*
 * petle_01.cpp
 */


#include <iostream>
using namespace std;

int cw01()
{
    int suma = 0;
    for(int i=10; i<100; i=i+2){
        suma += i;
        }
    cout << suma << endl;

    return suma;
}

void cw02()
{
    int a;
    cout << "Podaj liczbę całkowitą: " << endl;
    cin >> a;
}

void cw03()
{
    int a;
    int suma = 0;
    int sum = 0;
    int srednia;
    
    for(int i=0;i <8;i++){
        cout << "Podaj liczbę całkowitą: " << endl;
        cin >> a;
        suma = suma+a;
        srednia = suma/2;
        if(a%5== 0)sum = sum+1;
    }
    cout << suma << endl;
    cout << srednia << endl;
    cout << sum << endl;
    
}

int main(int argc, char **argv)
{
    cw03();
	return 0;
}

