# !/usr/bin/env pypy3
import sys
input = sys.stdin.readline
N=int(input())
S = [input().replace("\n","")for i in range(N)]
X, Y = input().split()
X = int(X)
if S[X-1] == Y:
    print("Yes")
else:
    print("No")