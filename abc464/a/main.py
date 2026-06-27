# !/usr/bin/env pypy3
import sys
input = sys.stdin.readline
S = input()
e = 0
w = 0
for s in S:
    if s == 'E':
        e+=1
    elif s == 'W':
        w+=1
if e > w:
    print("East")
else:
    print("West")