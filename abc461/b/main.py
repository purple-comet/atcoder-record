# !/usr/bin/env pypy3
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = True
for i in range(n):
    if a[i] != b.index(i+1) + 1:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")