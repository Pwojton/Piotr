@@ -10,14 +10,20 @@
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
            else {
@@ -66,6 +72,7 @@ int main(int argc, char **argv)
    //int ilosc = cin.gcount();
    //ilosc = zlicz(znaki);
    int ilosc = strlen(znaki);
    ascii(znaki, ilosc);
    //~ascii(znaki, ilosc);
    odwroc(znaki, ilosc);
    return 0;
}
