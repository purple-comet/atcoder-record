# !/usr/bin/env pypy3
import sys
import itertools
input = sys.stdin.readline
N, K, X = map(int, input().split())
S = [input() for i in range(N)]
A = list(itertools.product([i+1 for i in range(N)], repeat=K))
all_str = []
for arr in A:
    all_str.append("".join([S[i-1].replace("\n", "") for i in arr]))
all_str.sort()
print(all_str[X-1])