#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    int N;
    long long H;
    cin >> N >> H;
    
    int cal;
    cal = 0;
    long long nextH;
    int ans;
    ans = 0;
    
    for (int i=0; i<N-1; i++) {
      cin >> nextH;
      if (H >= nextH) {
        cal ++;
      } else {
        ans = max(ans, cal);
        cal = 0;
      }
      H = nextH;
    }
    ans = max(ans, cal);
    cout << ans << endl;

    return 0;
}
