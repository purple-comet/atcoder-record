# !/usr/bin/env pypy3
import sys
input = sys.stdin.readline
A = []
X,Y = map(int,input().split())
A.append(X)
A.append(Y)
for i in range(2,10):
    rev = reversed(str(A[i-1]+A[i-2]))
    ai = ""
    for r in rev:
        ai += r
    A.append(int(ai))
print(A[9])