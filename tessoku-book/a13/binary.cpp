#include <bits/stdc++.h>
using namespace std;
using ll = long long;
ll N, K;
vector<ll> A(100009);
int search(int n) {
    int L=1, R=N;
    int M;
    while(L < R) {
        /*
        L=M+1, R=M-1の更新では、境界を検知できない
        a11ではA[M] == nとなるMがただ1つ存在することが確定している（かつA[M] != nの時は答えではない）ため、一致した瞬間にbreakだけでOK
        a13ではあるMが計算されてA[M] <= A[i]+K だった時に自身が答えになる可能性もあればそれより大きい答えになる可能性もある
        →左端の更新は自身を含めて取る必要がある（L=M更新）
        L←Mに更新しつつM = (L + R) / 2では無限ループになる（L=R=Mになって値が変化しない）
        「右端が欲しいならMは切り上げてL=M, R=M-1で更新」「左端が欲しいならMは切り捨ててL=M+1, R=Mで更新」と覚えるとよさそう
        */
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