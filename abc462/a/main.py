# !/usr/bin/env pypy3
import sys
input = sys.stdin.readline
s = input()
ans = []
for c in s:
    if c.isdecimal():
        ans.append(c)
print(''.join(ans))
