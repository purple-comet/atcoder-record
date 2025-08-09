# !/usr/bin/env pypy3
import sys
import re
input = sys.stdin.readline
S = input()
T = []
for i in range(len(S)-1):
    if i == 0:
        if S[i] == "#":
            T.append("#")
        else:
            T.append("o")
    else:
        if S[i] == "#":
            T.append("#")
        elif S[i-1] == "#":
            T.append("o")
        else:
            T.append(".")

print("".join(T))
