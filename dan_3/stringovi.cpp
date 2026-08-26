#include<bits/stdc++.h>
using namespace std;

vector< pair<int, int> > v;

int main(){
    string n="PERICA";
    cout << *(n.begin()) << endl;
    cout << n[n.size()-1] << endl;
    cout << n[n.length()-1] << endl;
    cout << *( n.end()-1 ) << endl;
}