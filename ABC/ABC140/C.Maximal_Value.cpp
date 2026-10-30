#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    int A, B, N, nextB;
    cin >> N;
    int ans = 0;
    
    cin >> B;
    ans += B;
    
    for (int i=0; i<N-2; i++) {
      cin >> nextB;
      if (B <= nextB) {
        ans += B;
      } else {
        ans += nextB;
      }
      B = nextB;
    }
    ans += nextB;
    if (N == 2) {
      ans *= 2;
    }
    
    cout << ans << endl;

    return 0;
}
