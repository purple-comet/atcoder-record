# !/usr/bin/env pypy3
from collections import deque
Q = int(input())
qs = [list(map(int, input().split())) for i in range(Q)]
dq = deque()
for q in qs:
    if q[0] == 1:
        dq.append((q[2],q[1]))
    else:
        result = 0
        k = q[1]
        while True:
            x, c = dq.popleft()
            result += min(c, k) * x
            if c < k:
                k -= c
                continue
            elif c == k:
                break
            else:
                dq.appendleft((x, c-k))
                break
        print(result)
