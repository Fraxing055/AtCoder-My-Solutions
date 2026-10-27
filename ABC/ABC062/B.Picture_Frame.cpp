#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    
    int H, W;
    cin >> H >> W;
    string A;
    
    for (int i=0; i<W+1; i++) {
      cout << '#' << "";
    }
    cout << '#' << '\n';
    for (int j=0; j<H; j++) {
      cout << '#' << "";
      cin >> A;
      cout << A << "";
      cout << '#' << '\n';
    }
    for (int l=0; l<W+1; l++) {
      cout << '#' << "";
    }
    cout << '#' << endl;

    return 0;
}
