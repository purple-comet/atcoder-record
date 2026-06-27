# !/usr/bin/env pypy3
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
c = [list(map(int, input().split())) for i in range(n)]
print(c)
cs = sorted(c, key=lambda x: x[1])
for i in range(n):
    a = set([c[i][0] for i in range(i)])
for i in range(m):
    a = [*a, c[i][2]]
    print(len(a))