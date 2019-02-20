#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

#define MAKS 100

void szyfruj(char tekst[], int klucz){
    klucz= klucz%26;
    int i =0;
    int kod = 0;
    while (tekst[i])
}

void deszyfruj(char tekst[], int klucz){
    klucz = klucz % 26;
    //int kod = 0;
    int ilosc = strlen(tekst);
    int kod;


    for(int i = 0; i < ilosc; i++){
        kod = (int)tekst[i];
        kod+=3;
        tekst[i] = char(kod);
        cout << tekst[i];
    }
    
}


int main(int argc, char **argv)
{
    char tekst[MAKS];
	int klucz = 0;
    
    cout << "Podaj tekst: " << endl;
    cin.getline(tekst, MAKS);
    
    cout << "Podaj klucz: " << endl;
    cin >> klucz;
    
    //szyfruj(tekst, klucz);
    deszyfruj(tekst, klucz);
	return 0;
}
