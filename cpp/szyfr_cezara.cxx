/*
 * szyfr_ceazara.cxx
 */


#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

#define MAKS 100

void deszyfruj(char tb[], int klucz){
    klucz = klucz % 26;
    int kod = 0, i = 0;
    while (tb[i] != '\0'){
        kod = (int) tb[i];
        if (tb[i] == ' ')
        {
            ;
        } else if (kod < 91) {
            kod -= klucz;
            if (kod < 65) kod += 26;
        } else {
            kod -= klucz;
            if (kod < 97) kod += 26;
        }

        cout << (char)kod;
        tb[i]= (char)kod;
        i++;
    }
    cout << endl;
}

void szyfruj(char tb[], int klucz){
    klucz = klucz % 26;
    int kod = 0;
    int i = 0;
    while (tb[i] != '\0'){
        kod = (int) tb[i];
        if (tb[i] == ' ')
        {
            ;
        } else if (kod < 91) {
            kod += klucz;
            if (kod > 90) kod -= 26;
        } else {
            kod += klucz;
            if (kod > 122) kod -= 26;
        }

        cout << (char)kod;
        tb[i]= (char)kod;
        i++;
    }
    cout << endl;
}


int main(int argc, char **argv)
{
    char tekst[MAKS];
	int klucz = 0;

    cout << "Podaj tekst: " << endl;
    cin.getline(tekst, MAKS);

    cout << "Podaj klucz: " << endl;
    cin >> klucz;


    deszyfruj(tekst, klucz);
	return 0;
}
