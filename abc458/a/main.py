# !/usr/bin/env pypy3
import sys
from collections import deque
input = sys.stdin.readline

s = input()
n = int(input())
print(s[n:-n-1])