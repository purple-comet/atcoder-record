#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll binary_search (vector<ll> a, ll x) {
    ll divisor = 2;
    ll index = a.size() / 2;
    while (true) {
        divisor *= 2;
        if (a[index] == x) {
            break;
        }
        else if (a[index] > x) {
            index -= (a.size() / divisor);
        }
        else {
            index += (a.size() / divisor);
        }
    }
    return index+1;
}

int main() {
    cout.setf(ios::unitbuf);
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll N, X;
    cin >> N >> X;
    vector<ll> A(N);
    for (ll i = 0; i < N; i++) cin >> A[i];
    ll ans = binary_search(A, X);
    cout << ans << "\n";
    return 0;
}