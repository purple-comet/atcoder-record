# !/usr/bin/env pypy3
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
count = 0
while(m != 0):
    m = n % m
    count += 1
print(count)