#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    int A1, A2, A3;
    cin >> A1 >> A2 >> A3;
    
    cout << min({abs(A1 - A2) + abs(A2 - A3), abs(A1 - A3) + abs(A3 - A2), abs(A2 - A3) + abs(A3 - A1), abs(A2 - A1) + abs(A1 - A3), abs(A3 - A1) + abs(A1 - A2), abs(A3 - A2) + abs(A2 - A1)}) << endl;

    return 0;
}
