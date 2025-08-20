#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  // 入力
  int N, Q;
  cin >> N >> Q;
  vector<ll> A(N);
  vector<ll> sumA(N+1);
  for (int i = 0; i < N; i++) cin >> A[i];
  sumA[0] = 0;
  for (int i = 1; i <= N; i++) {
    sumA[i] = sumA[i-1] + A[i-1];
  }
  for (int i = 0; i < Q; i++) {
    int L,R;
    cin >> L >> R;
    cout << sumA[R] - sumA[L-1] << "\n";
  }
  return 0;
}