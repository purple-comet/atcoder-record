#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll H,W;
  cin >> H >> W;
  vector<vector<int>> X(H,vector<int>(W));
  vector<vector<int>> sum(H+1,vector<int>(W+1, 0));

  for (ll i = 0; i < H; i++) {
    for (ll j = 0; j < W; j++) {
      cin >> X[i][j];
    }
  }
  
  for (ll i = 1; i < H+1; i++) {
    for (ll j = 1; j < W+1; j++) {
      sum[i][j] = X[i-1][j-1] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]; 
    }
  }
  ll Q;
  cin >> Q;
  for (ll i = 0; i < Q; i++) {
    ll A, B, C, D;
    cin >> A >> B >> C >> D;
    ll ans = sum[C][D] - sum[A-1][D] - sum[C][B-1] + sum[A-1][B-1];
    cout << ans << "\n";
  }
  return 0;
}