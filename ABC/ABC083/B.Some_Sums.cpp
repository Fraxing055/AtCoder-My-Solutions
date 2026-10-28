#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    int N, A, B;
    cin >> N >> A >> B;
    int ans, cal, k;
    ans = 0;
    
    for (int i=1; i<N+1; i++) {
      k = i;
      cal = 0;
      while (k>0) {
        cal += k % 10;
        k = k / 10;
      }
      if (A <= cal && cal <= B) {
        ans += i;
      }
    }
    
    cout << ans << endl;

    return 0;
}
