#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

template <typename T = ll> vector<T> in(int n) { vector<T> v(n); for (auto &x : v) cin >> x; return v; }
template <typename T = ll> vector<vector<T>> in(int h, int w) { vector<vector<T>> v(h, vector<T>(w)); for (auto &r : v) for (auto &x : r) cin >> x; return v; }
template <typename T> ll sum(const vector<T> &v) { return accumulate(v.begin(), v.end(), 0LL); }
template <typename T> void uniq_all(vector<T> &v) { sort(v.begin(), v.end()); v.erase(unique(v.begin(), v.end()), v.end()); }
template <typename T> void print_v(const vector<T> &v) { for (int i = 0; i < (int)v.size(); i++) cout << v[i] << (i + 1 == (int)v.size() ? "" : " "); cout << '\n'; }
void YesNo(bool b) { cout << (b ? "Yes" : "No") << '\n'; }

ll op(ll a, ll b) {return a ^ b; }
ll e() {return 0; }


int main() {
  cin.tie(nullptr);
  ios::sync_with_stdio(false);

  ll N, Q;
  cin >> N >> Q;
  auto A = in(N);
  
  segtree<ll, op, e> seg(A);
  
  for (int i=0; i<Q; i++) {
    int t;
    ll x, y;
    cin >> t >> x >> y;
    if (t == 1) {
      x--;
      seg.set(x, seg.get(x) ^ y);
    } else {
      cout << seg.prod(x-1, y) << "\n";
    }
  }

  return 0;
}
