#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll N;
  cin >> N;
  vector<int> A(N+9,0);
  for (int i = 0; i < N; i++) cin >> A[i];
  ll D;
  cin >> D;
  vector<int> cumL(N+1);
  vector<int> cumR(N+1);
  cumL[0] = 0;
  cumR[0] = 0;
  for (int i = 1; i <= N; i++) {
    cumL[i] = max(cumL[i-1] , A[i-1]);
    cumR[i] = max(cumR[i-1] , A[N-i]);
  }
  reverse(cumR.begin(), cumR.end());
  for (int i = 0; i < D; i++) {
    ll L, R;
    cin >> L >> R;
    int ans = max(cumL[L-1],cumR[R]);
    cout << ans << "\n";
  }
  return 0;
}