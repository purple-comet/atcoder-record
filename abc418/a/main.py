# !/usr/bin/env pypy3
import sys
input = sys.stdin.readline
N = input()
S = input()
if S[-4:-1] == "tea":
    print("Yes")
else:
    print("No")