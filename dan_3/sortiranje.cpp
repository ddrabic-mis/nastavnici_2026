#include<bits/stdc++.h>
using namespace std;

bool usporedba(const auto &a, const auto &b){
  if (a.second == b.second) {
    return a.first < b.first;
  }
  return a.second > b.second;
}

int main(){
  vector<pair<string, int>> v={{"Perica", 5}, {"Ivan", 5}, {"Marija", 4}, {"Ivan", 3}};
  // klasično sortiranje
  sort(v.begin(), v.end());
  // sortiranje po drugom elementu para
  sort(v.begin(), v.end(), 
  [](const auto &a, const auto &b){
      // a.second = 5; error
      if (a.second == b.second) {
        return a.first < b.first;
      }
      return a.second > b.second;
  });
  // sort(v.begin(), v.end(), usporedba );
  for (auto [ime, ocjena] : v) {
    cout << ime << " " << ocjena << endl;
  }
}