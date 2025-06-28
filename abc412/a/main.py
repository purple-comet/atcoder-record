# !/usr/bin/env pypy3
N = int(input())
tasks = [list(map(int, input().split())) for i in range(N)]
count = 0
for i in range(N):
    if tasks[i][0] < tasks[i][1]:
        count += 1
print(count)