# !/usr/bin/env pypy3
import sys
input = sys.stdin.readline
N, L, R = map(int,input().split())
S = input()
res = True
for i in range(L-1, R):
    if S[i] == "x":
        res = False

if res:
    print("Yes")
else:
    print("No")
