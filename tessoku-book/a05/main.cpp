#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  int N, K;
  cin >> N >> K;
  ll ans = 0;
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      int white = K - i - j;
      if (i==j || i == white || j == white || white <= 0) {
        continue;
      }
      if (white <= N) {
        ans += 1;
        // cout << i << " " << j << " " << white << "\n";
      }
    }
  }
  for (int i = 1; i <= N; i++) {
    int white = K - 2*i;
    if (white <= N && white > 0 ) {
      // cout << i << " " << i << " " << white << "\n";
      if (white == i) ans+=1;
      else ans+=3;
    }
  }
  cout << ans << "\n";
  return 0;
}
