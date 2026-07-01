# !/usr/bin/env pypy3
import sys
from collections import deque
input = sys.stdin.readline

def main():
    h, w = map(int, input().split())
    if h == 1 and w == 1:
        print(0)
        return
    if h == 1:
        y = [1, *[2]*(w-2), 1]
        print(*y)
        return
    if w == 1:
        for i in range(h):
            if i == 0 or i == h-1:
                print(1)
            else:
                print(2)
        return
    for i in range(h):
        if i == 0 or i == h-1:
            y = [2, *[3]*(w-2), 2]
            print(*y)
        else:
            y = [3, *[4]*(w-2), 3]
            print(*y)

main()