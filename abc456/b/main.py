# !/usr/bin/env pypy3
import sys
from collections import deque
import itertools
input = sys.stdin.readline

ap = [[0]*3 for i in range(3)]

for i in range(3):
    a = list(map(int, input().split()))
    for aij in a:
        if aij == 4:
            ap[i][0] += 1
        elif aij == 5:
            ap[i][1] += 1
        elif aij == 6:
            ap[i][2] += 1 

arr = [0, 1, 2]
pattern = 0
for per in list(itertools.permutations(arr)):
    pattern += ap[0][per[0]]*ap[1][per[1]]*ap[2][per[2]]
print((float)(pattern / 216))