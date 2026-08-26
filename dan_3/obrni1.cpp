#include<bits/stdc++.h>
using namespace std;

int main(){
    string n;
    cin>>n;
    cout << *(n.begin()) << endl;
    reverse(n.begin(), n.end());
    cout<<stoi(n)<<endl;
}