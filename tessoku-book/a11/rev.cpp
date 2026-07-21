#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int N, X;
vector<int> A(100009);

int search(int x){
    int L = 1, R = N;
    while(L <= R) {
        int M = (L + R) / 2;
        if (x < A[M]) R = M - 1;
        if (x == A[M]) return M;
        if (x > A[M]) L = M + 1;
    }
    return -1;
}

int main() {
    cout.setf(ios::unitbuf);
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> X;
    for (int i = 1; i <= N; i++) cin >> A[i];
    int Answer = search(X);
    cout << Answer << "\n";
    return 0;
}