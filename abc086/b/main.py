# !/usr/bin/env pypy3
import sys
import math
def judge_sqrt_integer():
    input = sys.stdin.readline
    a, b = input().split()
    num = int(a + b)
    return math.sqrt(num).is_integer()

if judge_sqrt_integer():
    print("Yes")
else:
    print("No")