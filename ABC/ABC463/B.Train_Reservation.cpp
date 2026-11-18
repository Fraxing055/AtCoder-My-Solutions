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

int main() {
  cin.tie(nullptr);
  ios::sync_with_stdio(false);

  int N;
  string X;
  cin >> N >> X;
  bool F = false;
  
  for (int i=0; i<N; i++) {
    string S;
    cin >> S;
    if (X == "A" && S[0] == 'o') {
      F = true;
      break;
    } else if (X == "B" && S[1] == 'o') {
      F = true;
      break;
    } else if (X == "C" && S[2] == 'o') {
      F = true;
      break;
    } else if (X == "D" && S[3] == 'o') {
      F = true;
      break;
    } else if (X == "E" && S[4] == 'o') {
      F = true;
      break;
    }
  }
  
  YesNo(F);

  return 0;
}
