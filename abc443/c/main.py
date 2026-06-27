# !/usr/bin/env pypy3
import sys
input = sys.stdin.readline
n, t = map(int, input().split())
a = [0, *list(map(int, input().split())), t]
# print(a)
open_total = 0
close_time = 0
for i in range(1, n+2):
    if i == 1:
        open_total += a[1]
        close_time = a[1]
        continue
    # print(close_time)
    # print(max(a[i] - close_time - 100, 0))
    open_total += max(a[i] - close_time - 100, 0)
    # print(open_total)
    # print()
    close_time = min(a[i], close_time) if a[i] - close_time < 100 else a[i]
print(open_total)