#include <bits/stdc++.h>
using namespace std;
using ll = long long;
ll N, K;
vector<ll> A(100009);
int search(int n) {
    int L=1, R=N;
    int M;
    while(L < R) {
        M = (L + R + 1) / 2;
        if (A[M] <= n) L = M;
        if (A[M] > n) R = M - 1;  
    }
    return R;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> K;
    for (ll i = 1; i <= N; i++) cin >> A[i];
    ll sum = 0;
    for (ll i = 1; i <= N; i++) {
        ll index = search(A[i] + K);
        sum += index - i;
    }

    cout << sum << "\n";
    return 0;
}