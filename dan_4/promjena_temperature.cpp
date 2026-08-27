#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    /*
    int* p1=nullptr; // pokazivac na ništa
    int* p2=&n; // pokazivac na n
    int &r=n; // referenca na n
    */
    cin >> n;
    vector<int> v;
    int brojac=0;
    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        if (i && x > *(v.end()-1)){
            brojac++;
        } 
        //v.push_back(x);
        v.emplace_back(x);
        /*
        if (i && v[i] > v[i-1]){
            brojac++;
        } 
        */
    }
    /*
    // brojanje koliko puta je temperatura porasla
    for (int i = 1; i < n; i++){
        if (v[i] > v[i-1]){
            brojac++;
        }
    }
    */
    cout << brojac << endl;
}