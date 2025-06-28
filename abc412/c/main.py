# !/usr/bin/env pypy3
T = int(input())
N_input = []
S_input = []
for i in range(T):
    N = int(input())
    N_input.append(N)
    S = list(map(int, input().split()))
    S_input.append(S)
for i in range(len(N_input)):
    domino = S_input[i][0]
    count = 1
    while domino < S_input[i][-1]:
        next = list(filter(lambda x: domino < x <= 2 * domino, S_input[i]))
        print(next)
        if len(next) == 0:
            print(-1)
            break
        else:
            count += 1
            domino = max(next)
    else:
        print(count)
