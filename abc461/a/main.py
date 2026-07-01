# !/usr/bin/env pypy3
import sys
from collections import deque
input = sys.stdin.readline

a,d = map(int, input().split())
if a <= d:
    print("Yes")
else:
    print("No")