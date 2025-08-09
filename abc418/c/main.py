# !/usr/bin/env pypy3
import sys
import bisect
input = sys.stdin.readline
N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = [int(input()) for _ in range(Q)]
sum_A = []
sum_A.append(0)
for i in range(len(A)):
    sum_A.append(sum_A[i] + A[i])
for b in B:
    if b > A[-1]:
        print(-1)
        continue
    threshold = bisect.bisect_left(A, b)
    res = sum_A[threshold] + b + (b - 1) * (N - threshold - 1)
    print(res)
