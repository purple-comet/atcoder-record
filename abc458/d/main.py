# !/usr/bin/env pypy3
import sys
from collections import deque
import math
input = sys.stdin.readline

x = int(input())
q = int(input())
window = [0, 0, x, math.inf, math.inf]
for i in range(q):
    a, b = map(int, input().split())
    mid = window[2]
    shift = 0
    if mid < a and mid < b:
        shift = 1
    elif mid > a and mid > b:
        shift = -1
    window.append(a)
    window.append(b)
    window.sort()
    print(window)
    window = window[(1+shift):(6+shift)]
    print(window)
    print(window[2])