#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll H,W,N;
  cin >> H >> W >> N;
  vector<vector<int>> R(H+9,vector<int>(W+9, 0));
  vector<vector<int>> Col(H+9,vector<int>(W+9, 0));
  vector<vector<int>> cum(H+9,vector<int>(W+9, 0));
  

  for (ll i = 0; i < N; i++) {
    int A, B, C, D;
    cin >> A >> B >> C >> D;
    R[A][B] += 1;
    R[A][D+1] -= 1;
    for (int j = B; j <= D; j++) {
      Col[C+1][j] -= 1;
    }
  }
  
  for (int i = 1; i <= H; i++) {
    for (int j = 1; j <= W; j++) {
      cum[i][j] += cum[i][j-1] + R[i][j];
    }
  }
  

  for (int j = 1; j <= W; j++) {
    for (int i = 1; i <= H; i++) {
      cum[i][j] += cum[i-1][j] + Col[i][j];
    }
  }

for (int i = 1; i <= H; i++) {
    for (int j = 1; j <= W; j++) {
      cout << cum[i][j] << " ";
    }
    cout << "\n";
  }
  cout << "\n";
  return 0;
}