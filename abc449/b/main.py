# !/usr/bin/env pypy3
import sys
input = sys.stdin.readline
n = int(input())
costs = [list(map(int, input().split())) for i in range(n-1)]

ans = False
for a in range(n):
    for c in range(a+2, n):
        for b in range(a+1,c):
            if costs[a][b-a-1] + costs[b-a][c-a-b-1] < costs[a][c-a-1]:
                ans = True

if ans:
    print('Yes')
else:
    print('No')