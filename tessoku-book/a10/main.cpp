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
  vector<int> cum_l(N+1);
  vector<int> cum_r(N+1);
  cum_l[0] = 0;
  cum_r[0] = 0;
  for (int i = 1; i <= N; i++) {
    cum_l[i] = max(cum_l[i-1] , A[i-1]);
    cum_r[i] = max(cum_r[i-1] , A[N-i]);
  }
  reverse(cum_r.begin(), cum_r.end());
  for (int i = 0; i < D; i++) {
    ll L, R;
    cin >> L >> R;
    int ans = max(cum_l[L-1],cum_r[R]);
    cout << ans << "\n";
  }
  return 0;
}