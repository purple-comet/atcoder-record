# !/usr/bin/env pypy3
import sys
input = sys.stdin.readline
n = int(input())
gift = [list(map(int,input().split())) for _ in range(n)]
gifted = [[0] for _ in range(n)]
for i in range(n):
    for v in gift[i][1:]:
        gifted[v-1][0] += 1
        gifted[v-1].append(i+1)
ans = []
for g in gifted:
    ans.append([g[0], *sorted(g[1:])])
for a in ans:
    for v in a:
        print(v, end=' ')
    print()