/*
 * szabloncpp.cpp
 */


#include <iostream>     

using namespace std; //domyślną biblioteką jest standardowa

int main(int argc, char **argv)
{
	int a; //deklaracja zmiennej
    a = 0; //inicjacja zmiennej  
    cout << "Podaj liczbę: "; //stały napis
    cin >> a;  //podaj a
    cout << a;  //zwróć a
	return 0;
}

