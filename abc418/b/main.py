# !/usr/bin/env pypy3
import sys
input = sys.stdin.readline
S = input()
res = 0
for i in range(len(S)):
    for j in range(i + 3, len(S)):
        part = S[i:j]
        if part[0] == "t" and part[-1] == "t":
            res_temp = (part.count("t") - 2) / (len(part) - 2)
            if res_temp > res:
                res = res_temp
print(res)
