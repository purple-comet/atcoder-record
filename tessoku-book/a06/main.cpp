#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  // 入力
  int N, Q;
  cin >> N >> Q;
  vector<ll> A(N);
  vector<ll> sum_a(N+1);
  for (int i = 0; i < N; i++) cin >> A[i];
  sum_a[0] = 0;
  for (int i = 1; i <= N; i++) {
    sum_a[i] = sum_a[i-1] + A[i-1];
  }
  for (int i = 0; i < Q; i++) {
    int L,R;
    cin >> L >> R;
    cout << sum_a[R] - sum_a[L-1] << "\n";
  }
  return 0;
}