# !/usr/bin/env pypy3
import sys
input = sys.stdin.readline
N=int(input())
S=list(input())
count=0
acc = [0] * (N+1)
for i in range(N):
    acc[i+1] = acc[i] + i

def divide(input_str):
    a=0
    b=0
    ret = []
    ind=0
    for i in range(len(input_str)):
        if input_str[i] == "A":
            a+=1
        else:
            b+=1

        if a==b:
            # print("app")
            # print(a, " ", b)
            ret.append(input_str[ind:i+1])
            ind=i+1
            continue
    return ret

def count_from_init(input_str,first):
    count=0
    indexes = [i+1 for i, x in enumerate(input_str) if x == first]
    # print("index")
    # print(indexes)
    for i in range(len(indexes)):
        count += indexes[i] - (i+1)
        # print("count")
        # print(count)
    return count
S_divided = divide(S)
ans=0
for s in S_divided:
    x = acc[int(len(s)/2)]
    z = 0
    if s[0] != S[0]:
        z = s.index(S[0])
        s[0], s[z] = s[z], s[0]
    y = count_from_init(s, S[0])

    # print()
    # print(s)
    # print(x)
    # print(y)
    # print(z)
    # print()
    ans += x-y+z
print(ans)
# ans = acc[N] - count_from_init(S_divided)
# while(True):
#     is_alternating = True
#     for i in range(1,2*N-1):
#         if S[i-1] == S[i] and S[i] != S[i+1]:
#             S[i], S[i+1] = S[i+1], S[i]
#             count+=1
#             is_alternating=False
#             break
#     print("".join(S))
#     if is_alternating == True:
#         break

"""
AAAABBBBなどの形は階差数列。
公差が1,2,3,4,...
0,1,3,6,10,15,21,....

Aから始まるやつで、ABの数が等しくなる部分文字列を取ると、必ずBで終わる

（部分文字列）BBBA…みたいなやつは、Bの数だけ反転させればAから始まる文字列にできる


"""