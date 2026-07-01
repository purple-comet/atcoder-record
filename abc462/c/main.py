# !/usr/bin/env pypy3
import sys
input = sys.stdin.readline
n = int(input())
p_raw = [list(map(int, input().split())) for _ in range(n)]
p = sorted(p_raw, key=lambda x: x[0])
x = [p[i][0] for i in range(n)]
y = [p[i][1] for i in range(n)]
count = 1
for i in range(1, n):
    y_i = sorted(y[:i])
    # ↑TLEポイント 実は最小値を毎回更新する必要はない。
    # 次の点では今まで扱った点+自分が対象になるだけなので、y_minはy_minと自分のy座標の最小値を調べることで求められる
    y_min = y_i[0]
    if y_min >= p[i][1]:
        count += 1
print(count)