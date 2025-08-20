#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  int N, X;
  cin >> N >> X;
  bool ans = false;
  vector<ll> A(N);
  for (int i=0; i < N; i++) cin >> A[i];
  for (int i=0; i < N; i++) {
    if (A[i] == X) ans = true;
  }
  if (ans == true) cout << "Yes" << "\n";
  else cout << "No" << "\n";
  return 0;
}