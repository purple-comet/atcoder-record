# !/usr/bin/env pypy3
import sys
from collections import deque
input = sys.stdin.readline

s = input()
n = len(s)
ans = 0
for i in range(n-1):
    if s[i] == 'C':
        ans += min(i+1, n-i-1)
print(ans)