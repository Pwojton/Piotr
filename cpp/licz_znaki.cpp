/*
 * znaki.cpp
 * 
 * char - typ danej zawierający jeden znak
 */


#include <iostream>

using namespace std;

void zamien_znaki(char tb[], int roz) {
    for(int i = 0; i < roz; i ++) {
        
    }
    
}

void licz_znaki(char tb[], int roz)
{
    int i = 0;
    int cyfry, literyD, literyM, reszta;
    cyfry = literyD = literyM = reszta = 0;
    
    int znak_kod = 0; // kod ASCII badanego znkau
    while (tb[i] != '\0') {
        if(znak_kod > 64 && znak_kod < 91)
            literyD++;
        else if (znak_kod > 97 && znak_kod < 122)
            literyM++;
        else if(znak_kod > 48 && znak_kod < 57)
            cyfry++;
        else
            reszta++;
    };
    cout << "LiteryD " << literyD << "LiteryM " << literyM << "Cyfry " << cyfry << endl; 
}

int main(int argc, char **argv)
{
    const int rozmiar = 20;
	char znaki[rozmiar];
    cin.getline(znaki, rozmiar);
    licz_znaki(znaki, cin.gcount());
	return 0;
}

