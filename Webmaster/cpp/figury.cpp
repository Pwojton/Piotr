/*
 * figury.cpp
 * code blocks - program z kompilatorem cpp na windowsa
 */


#include <iostream>
using namespace std;

void prostokat(int x, int y, char znak){
    for (int i = 0; i < x; i++){
        for (int j = 0; j < y; j++)
            if (j == 0 || j == y - 1 || i == 0 || i == x - 1)
                cout << znak;
            else
                cout << " ";
        cout << endl;
    }
}

int main(int argc, char **argv)
{
	int a, b; //deklaracja
    a = b = 0; //inicjacja
    // int a = 0; //defincja
    cout << "Podaj bok1: ";
    cin >> a;
    cout << "Podaj bok2: ";
    cin >> b;
    
    char znak;
    cout << "Podaj znak: ";
    cin >> znak;
    
    prostokat(a, b, znak);
	return 0;
}

