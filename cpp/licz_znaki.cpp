using namespace std;
void odwroc(char tb[], int roz){
        for(int i = roz; i >= 0; i--)
            cout << tb[i] << " ";
    }
void ascii(char tb[], int roz) {
        int kod = 0;
        for(int i = 0; i < roz; i++){
            kod = (int)tb[i];
            if (kod > 96 && kod < 123){
                cout << (char)(kod-32) << " ";
                }
            else if (kod > 64 && kod < 92){
            else if (kod > 64 && kod < 91){
                cout << (char)(kod+32) << " ";
                }
            }
            else {

         }
     cout << "\n\nmałe: " << literyM << endl;
     cout << "duże: " << literyD << endl;
     cout << "cyfry: " << cyfry << endl;
     cout << "Inne: " << reszta << endl;
 }
 
 int zlicz(char tb[]){
     int i = 0;
     while (tb[i] != '\0') {
         i++;
         }
     return i;
     }
 
 int main(int argc, char **argv)
 {
     const int rozmiar = 20;
     char znaki[rozmiar];
     cin.getline(znaki, rozmiar);
    //int ilosc = cin.gcount();
    //ilosc = zlicz(znaki);
    int ilosc = strlen(znaki);
    ascii(znaki, ilosc);
    //~ascii(znaki, ilosc);
    odwroc(znaki, ilosc);
    return 0;
}
