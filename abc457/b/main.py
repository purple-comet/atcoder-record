# !/usr/bin/env pypy3
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    l = list(map(int, input().split()))
    a.append(l[1:])
x, y = map(int, input().split())
print(a[x-1][y-1])