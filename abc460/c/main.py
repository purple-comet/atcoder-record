# !/usr/bin/env pypy3
import sys
from collections import deque
import bisect
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = [n * 2 for n in a]
a.sort()
b.sort(reverse=True)
count = 0
for i in range(m):
    pos = bisect.bisect_left(a, b[i])
    pair = n - pos
    pair_rest = pair - count
    if pair_rest > 0:
        count+=1
print(count)

