#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  int N, K;
  cin >> N;
  vector<ll> ans;
  int process_num = N;
  int q = 2;
  while(true) {
    if (process_num % 2 == 0) {
      ans.push_back(0);
      process_num = process_num / 2;
    }
    else {
      ans.push_back(1);
      process_num = (process_num - 1) / 2;
    }
    if (process_num < 1) break; 
  }
  for (int i = ans.size(); i < 10; i++) ans.push_back(0);
  reverse(ans.begin(), ans.end());
  for (int i = 0; i < ans.size(); i++) cout << ans[i] << "";
  cout << "\n";
  return 0;
}