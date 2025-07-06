# !/usr/bin/env pypy3
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
S = input()

def accumulate_S(s, len_S):
    acc_num = 0
    acc_array = []
    for i in range(len_S):
        if i >= 1 and "".join((s[i-1], s[i])) == "AC":
            acc_num += 1
        acc_array.append(acc_num)
    return acc_array

acc = accumulate_S(S, N)
def count_ac(acc_array, l, r):
    return acc_array[r-1] - acc_array[l-1]

for i in range(Q):
    l, r = map(int, input().split())
    print(count_ac(acc, l, r))