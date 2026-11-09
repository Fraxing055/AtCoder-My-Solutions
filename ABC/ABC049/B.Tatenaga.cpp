#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    string pic;
    int H, W;
    cin >> H >> W;
    
    for (int i=0; i<H; i++) {
      cin >> pic;
      cout << pic <<'\n' << pic << '\n';
    }

    return 0;
}
