# !/usr/bin/env pypy3
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())
print(a[x-1])