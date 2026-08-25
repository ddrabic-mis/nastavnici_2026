/*
Učitajte neki tekst te ispišite slovo koje se najviše puta ponavljalo i slovo koje se najmanje puta pojavilo. Sva sova biti će mala engleske abecede.
ako se više takvih slova pojavi, ispiši samo ono leksikografski prvo.
ULAZ
kjhdjk432,mn!kas   sefff
IZLAZ
*/

#include<bits/stdc++.h>
using namespace std;

int main() {
    string s;
    getline(cin, s); // učitavanje cijelog reda teksta (i s prazninama)
    // int F[26] = {0}; // array 
    vector<int> F(26, 0);
    char min_slovo, max_slovo;
    int min_cnt=INT_MAX, max_cnt=0;
    for (auto c : s) {
        if (c >= 'a' && c <= 'z') {
            F[c - 'a']++;
            // utvrdimo najmanji broj ponavljanja i najveći broj ponavljanja nekog slova
            if (F[c - 'a'] > max_cnt) {
                max_cnt = F[c - 'a']; // pamtimo broj pojavljivanja
                max_slovo = c; // pamtimo to slovo
            }
            else if (F[c - 'a'] == max_cnt && c < max_slovo) {
                max_slovo = c; // pamtimo to slovo  
            }

            if (F[c - 'a'] < min_cnt) {
                min_cnt = F[c - 'a']; // pamtimo broj pojavljivanja
                min_slovo = c; // pamtimo to slovo
            }
            else if (F[c - 'a'] == min_cnt && c < min_slovo) {
                min_slovo = c; // pamtimo to slovo  
            }            
        }
    }
    // IZLAZ
    /*
    for (int i = 0; i < 26; i++) {
        if (F[i] > 0) {
            cout << char(i + 'a') << " " << F[i] << endl;
        }
    }
    */
   cout << max_slovo << " " << min_slovo << endl;
   cout << max_cnt << " " << min_cnt << endl;

    return 0;
}