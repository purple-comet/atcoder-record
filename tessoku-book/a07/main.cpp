#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  int D,N;
  cin >> D >> N;
  vector<ll> A(D);
  for (int i = 0; i < N; i++) {
    ll L,R;
    cin >> L >> R;
    for (int j = L-1; j < R; j++) {
      A[j] += 1;
    }
  }
  for (int i = 0; i < D; i++) cout << A[i] << "\n";
  return 0;
}