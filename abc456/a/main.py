# !/usr/bin/env pypy3
import sys
from collections import deque
input = sys.stdin.readline

x=int(input())
print("Yes" if x >= 3 and x <= 18 else "No")