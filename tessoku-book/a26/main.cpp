#include <bits/stdc++.h>
using namespace std;
using ll = long long;

bool isPrime(int x){
    bool isPrime = true;
    for (int i = 2; i * i <= x; i++) {
        if (x % i == 0){
            isPrime = false;
            break;
        }
    }
    return isPrime;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> X(10000);

    int Q;
    cin >> Q;
    for (int i = 0; i < Q; i++){
        cin >> X[i];
    }
    for (int i = 0; i < Q; i++){
        bool ans = isPrime(X[i]);
        if (ans){
            cout << "Yes" << "\n";
        } else {
            cout << "No" << "\n";
        }
    }
    return 0;
}