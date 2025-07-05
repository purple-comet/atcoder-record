# !/usr/bin/env pypy3
N = int(input())
S = [input() for i in range(N)]
word_to_count = {}
for i in range(N):
    for j in range(N - i - 1):
        word1 = S[i] + S[i + j + 1]
        word2 = S[i + j + 1] + S[i]
        if not word_to_count.get(word1):
            word_to_count[word1] = 1
        if not word_to_count.get(word2):
            word_to_count[word2] = 1
print(len(word_to_count))