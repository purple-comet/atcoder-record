# !/usr/bin/env pypy3
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
s = input().split()
ans = []
for si in s:
    c = si[0]
    if 'a' <= c and c < 'd':
        ans.append('2')
    elif 'd' <= c and c < 'g':
        ans.append('3')
    elif 'g' <= c and c < 'j':
        ans.append('4')
    elif 'j' <= c and c < 'm':
        ans.append('5')
    elif 'm' <= c and c < 'p':
        ans.append('6')
    elif 'p' <= c and c < 't':
        ans.append('7')
    elif 't' <= c and c < 'w':
        ans.append('8')
    elif 'w' <= c and c <= 'z':
        ans.append('9')
print("".join(ans))