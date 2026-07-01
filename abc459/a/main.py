# !/usr/bin/env pypy3
import sys
from collections import deque
input = sys.stdin.readline

x = int(input())
s = "HelloWorld"
ans = []
for i in range(len(s)):
    if i == x - 1:
        continue
    ans.append(s[i])
print("".join(ans))