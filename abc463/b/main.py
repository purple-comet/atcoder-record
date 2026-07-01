# !/usr/bin/env pypy3
import sys
input = sys.stdin.readline
n, x = input().split()
n = int(n)
s = [input() for i in range(n)]
column = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
emp = False
for inf in s:
    if inf[column[x]] == 'o':
        emp = True
if emp:
    print("Yes")
else:
    print("No")