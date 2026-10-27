#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    int A, B;
    cin >> A >> B;
    int count;
    count = 0;
    string k;
    
    for (int i=A; i<B+1; i++) {
      k = to_string(i);
      if (k[0] == k[4] && k[1] == k[3]) {
        count ++;
      }
    }
    
    cout << count << endl;

    return 0;
}
