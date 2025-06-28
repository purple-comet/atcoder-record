# !/usr/bin/env pypy3
[N, Q] = list(map(int, input().split()))
queries = list(map(int, input().split()))
panels = [False for i in range(N+2)]
count = 0
for i in range(Q):
    if panels[queries[i]] == False:
        panels[queries[i]] = True
        if panels[queries[i] - 1] == False and panels[queries[i] + 1] == False:
            count += 1
        elif panels[queries[i] - 1] == True and panels[queries[i] + 1] == True:
            count -= 1
    else:
        panels[queries[i]] = False
        if panels[queries[i] - 1] == False and panels[queries[i] + 1] == False:
            count -= 1
        if panels[queries[i] - 1] == True and panels[queries[i] + 1] == True:
            count += 1
    print(count)
