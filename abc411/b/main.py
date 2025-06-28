# !/usr/bin/env pypy3
n = int(input())
dis = list(map(int,input().split()))
for i in range(n-1):
    res = []
    for j in range(n-i-1):
        res.append(str(sum(dis[i:i+j+1])))
    print(" ".join(res))