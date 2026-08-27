#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    int prethodna, brojac=0;
    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        if (i && x > prethodna){
            brojac++;
        }
        prethodna = x;
    }
    cout << brojac << endl;
}