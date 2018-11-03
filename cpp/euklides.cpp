/*
 * euklides.cpp
 * 
 * Copyright 2018  <>
 */
 

#include <iostream>
using namespace std;

int nwd_optymalny(int a, int b)
{
    int licznik = 0;
    while(a > 0)
    {
        a = a%b;
        b = b - a;
        licznik++;
    }
    cout << "Powtórzeń: " << licznik << endl;
    return b;
}

int nwd_klasyczny(int a, int b)
{
    int licznik = 0;
    while(a > b)
    {
        if(a > b)
            a = a - b;
        else 
            b = b - a;
        licznik++;
    }
    cout << "Powtórzeń: " << licznik << endl;
    return a;
}
int main(int argc, char **argv)
{
	int a, b;
    cout << "Podaj dwe liczby: ";
    cin >> a >> b;
    int nwd = nwd_klasyczny(a, b);
    cout << "NWD(" << a << "," << b << ") =" << nwd << endl; 
    nwd = nwd_optymalny(a, b);
	return 0;
}

