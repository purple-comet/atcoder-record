# !/usr/bin/env pypy3
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
l = [a[i][0] for i in range(n)]
c = list(map(int, input().split()))
it = 0
while(True):
    add_length = c[it] * l[it]
    if k <= add_length:
        index = k % l[it] if k % l[it] != 0 else l[it]
        print(a[it][index])
        break
    k -= add_length
    it += 1