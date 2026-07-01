# !/usr/bin/env pypy3
import sys
input = sys.stdin.readline
x, y = map(int, input().split())
if x * 9 / 16 == y:
    print("Yes")
else:
    print("No")