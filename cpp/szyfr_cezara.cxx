#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

#define MAKS 100

void szyfruj(char tekst[], int klucz){
    klucz = klucz % 26;
    int kod = 0;
    int ilosc = strlen(tekst);
    
    for(int i = 0; i < ilosc; i++){
        kod = (int)tekst[i];
        kod += klucz;
        if (tekst[i] == ' ') {
            kod -= klucz;
            }
        else if(kod > 122){
            kod -= 26;
        }
        tekst[i] = char(kod);
        cout << tekst[i];
    }

}

void deszyfruj(char tekst[], int klucz){
    klucz = klucz % 26;
    //int kod = 0;
    int ilosc = strlen(tekst);

    for(int i = 0; i < ilosc; i++){
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
    
    szyfruj(tekst, klucz);
	return 0;
}
