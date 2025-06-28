# !/usr/bin/env pypy3
S = input()
T = input()
result = True
chrs_before_cap = []
for i in range(len(S)):
    if i == 0:
        continue
    elif ord("A") <= ord(S[i]) <= ord("Z"):
        chrs_before_cap.append(S[i-1])
for chr in chrs_before_cap:
    if T.find(chr) == -1:
        result = False
if result:
    print("Yes")
else:
    print("No")