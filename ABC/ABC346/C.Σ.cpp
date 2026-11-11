#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    
    long  N, K;
    cin >> N >> K;

    vector<long> A(N);
    for (auto &x : A) cin >> x;
    sort(A.begin(), A.end());
    
    long ans = 0;
    
    if (A.at(0) <= K) {
      ans = A.at(0);
      for (long i=0; i<N-1; i++) {
        if (A.at(i+1) > K) {
          break;
        }
        if (A.at(i) != A.at(i+1)) {
          ans += A.at(i+1);
        }
      }
    }
    
    long S = K * (1+K) / 2;
    
    cout << S - ans << endl;
    
    return 0;
}
