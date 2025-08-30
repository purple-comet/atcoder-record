import random
N=10000
print(N)
o=["A" for i in range(N)]
for i in range(N):
    o.append("B")
random.shuffle(o)
print("".join(o))