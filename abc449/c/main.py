# !/usr/bin/env pypy3
import sys
import numpy as np
input = sys.stdin.readline
h, w = list(map(int, input().split()))
s = [input()[0:-1] for i in range(h)]
    
hol_arr = []
for string in s:
    subarr = []
    for i in range(len(string)):
        if i == 0:
            subarr.append(0)
        elif string[i] == string[i-1]:
            subarr.append(0)
        elif string[i] == '#' and string[i-1] == '.':
            subarr.append(-1)
        elif string[i] == '.' and string[i-1] == '#':
            subarr.append(1)
    hol_arr.append(subarr)
        
ver_arr_t =[]
for i in range(h):
    sub_arr = []
    for j in range(w):
        if i == 0:
            sub_arr.append(0)
        elif s[i][j] == s[i-1][j]:
            sub_arr.append(0)
        elif s[i][j] == '#' and s[i-1][j] == '.':
            sub_arr.append(-1)
        elif s[i][j] == '.' and s[i-1][j] == '#':
            sub_arr.append(1)
    ver_arr_t.append(sub_arr)
        

ver_arr = [list(x) for x in zip(*ver_arr_t)]

count = 0
for i in range(h):
    hol1 = [x for x, y in enumerate(hol_arr[i]) if y == 1]
    hol_1 =[x for x, y in enumerate(hol_arr[i]) if y == -1]
    for j in range(len(hol1)):
        if len(hol1) != len(hol_1) and j == len(hol_arr) - 1:
            continue
        h = hol_1[j]
        t1 = False
        for k in range(j,h):
            ver1 = [x for x, y in enumerate(ver_arr[i]) if y == 1]
            ver_1 =[x for x, y in enumerate(ver_arr[i]) if y == -1]
            t = False
            for l in range(len(ver1)):
                if ver1[l] <= i and i <= ver_1[l]:
                    t = True
            if t:
                t1 = True
        if t1:
            count += 1


           
print(count)