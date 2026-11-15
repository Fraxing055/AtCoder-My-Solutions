#include <bits/stdc++.h>
using namespace std;
using ll = long long;

template <typename T = ll> vector<T> in(int n) { vector<T> v(n); for (auto &x : v) cin >> x; return v; }
template <typename T = ll> vector<vector<T>> in(int h, int w) { vector<vector<T>> v(h, vector<T>(w)); for (auto &r : v) for (auto &x : r) cin >> x; return v; }
template <typename T> ll sum(const vector<T> &v) { return accumulate(v.begin(), v.end(), 0LL); }
template <typename T> void uniq_all(vector<T> &v) { sort(v.begin(), v.end()); v.erase(unique(v.begin(), v.end()), v.end()); }
template <typename T> void print_v(const vector<T> &v) { for (int i = 0; i < (int)v.size(); i++) cout << v[i] << (i + 1 == (int)v.size() ? "" : " "); cout << '\n'; }
void YesNo(bool b) { cout << (b ? "Yes" : "No") << '\n'; }

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    int N;
    cin >> N;
    int ans = 0;
    
    for (int i=1; i<N+1; i++) {
      int C = i;
      int D = 0;
      while (C != 0) {
        C = C / 10;
        D++;
      }
      if (D % 2 == 1) {
        ans++;
      }
    }
    cout << ans << '\n';

    return 0;
}
