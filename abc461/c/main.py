# !/usr/bin/env pypy3
import sys
from collections import deque
input = sys.stdin.readline

n, k, m = map(int, input().split())
crystal = [list(map(int, input().split())) for _ in range(n)]

sorted_c = sorted(crystal,reverse=True, key=lambda x: x[1])
used_color = set()
ans=0
j = 0
while(len(used_color) <= k-m and j < k-1):
    print(used_color)
    print(*sorted_c[j])
    used_color.add(sorted_c[j][0])
    ans += sorted_c[j][1]
    j+=1

rest = sorted_c[j:]
c_max = {}
print(rest)
if len(rest) > 0:
    for i in range(n):
        c_max[rest[i][0]] = max(c_max.get(rest[i][0]) if c_max.get(rest[i][0]) is not None else 0 , rest[i][1])
    s_c_max = sorted(c_max.items(), reverse=True, key=lambda x: x[1])
    print(c_max)
    print(s_c_max)
    l=0
    while(j+l >= n):
        print(c_max[l])
        print(c_max[l][1])
        l += 1
        ans += c_max[l][1]

print(ans)
