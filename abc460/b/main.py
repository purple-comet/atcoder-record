# !/usr/bin/env pypy3
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d2 = (x2-x1) ** 2 + (y2-y1) ** 2
    if d2 > (r1 + r2) ** 2 or d2 < (max(r1, r2) - min(r1, r2)) ** 2:
        print("No")
    else:
        print("Yes")
