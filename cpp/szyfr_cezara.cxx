#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

#define MAKS 100

void szyfruj(char tekst_jawny[], int klucz){
    
    int ilosc = strlen(tekst_jawny);
    int kod;
    
    for(int i = 0; i < ilosc; i++){
        kod = (int)tb[i];
            
    }

}


int main(int argc, char **argv)
{
    char tekst_jawny[MAKS];
	int klucz = 0;
    
    cout << "Podaj tekst: " << endl;
    cin.getline(tekst_jawny, MAKS);
    
    cout << "Podaj klucz: " << endl;
    cin >> klucz;
    
    szyfruj(tekst_jawny, klucz);
	return 0;
}
