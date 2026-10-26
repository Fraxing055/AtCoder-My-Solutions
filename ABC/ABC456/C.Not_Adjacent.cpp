#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    
    string S;
    cin >> S;
    
    const long long MOD = 998244353;
    long long ans = 1;
    long long len = 1;
    
    for (int i=1; i<(int)S.size(); i++) {
      if (S[i] == S[i-1]) {
        len = 1;
      } else {
        len++;
      }
      ans = (ans + len) % MOD;
    }
    
    cout << ans << endl;

    return 0;
}
