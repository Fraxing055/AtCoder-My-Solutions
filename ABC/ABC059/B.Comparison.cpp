#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    string A, B;
    cin >> A >> B;
    if (A == B) {
      cout << "EQUAL" << endl;
    } else {
      if (A.size() > B.size()) {
        cout << "GREATER" << endl;
      } else if (A.size() < B.size()) {
        cout << "LESS" << endl;
      } else {
        if (A > B) {
          cout << "GREATER" << endl;
        } else {
          cout << "LESS" << endl;
        }
      }
    }

    return 0;
}
