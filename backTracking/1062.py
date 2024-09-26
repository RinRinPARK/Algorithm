import sys


N, K = map(int, sys.stdin.readline().split())
words = []
basic = {'a', 'n', 't', 'i', 'c'}
teach = ['a', 'n', 't', 'i', 'c']
candidate = set()
answer = 0


def dfs(num, k):
    global answer

    if len(teach) == k:
        cnt = 0
    
        for word in words:
            flag = 0

            for c in word:
                if c not in teach:
                    flag = 1
                    break
            if flag == 0:
                cnt += 1

        answer = max(answer, cnt)
        return 

    for i in range(num+1, len(candidate)):
        teach.append(candidate[i])
        dfs(i, k)
        teach.pop()
        

for _ in range(N):
    word = set(list(sys.stdin.readline().strip())) - basic
    for i in word:
        if (i not in candidate):
            candidate.add(i)
    words.append(word)

if K < 5:
    print(0)
    exit()

if K == 26:
    print(N)
    exit()

if len(candidate) <= K - 5:
    print(N)
    exit()

candidate = list(candidate)
for j in range(len(candidate)):
    teach.append(candidate[j])
    dfs(j, K)
    teach.pop()

print(answer)




"""
combinations 이용 코드


import sys
from itertools import combinations


N, K = map(int, sys.stdin.readline().split())
words = []
basic = {'a', 'n', 't', 'i', 'c'}
teach = set()
answer = 0
        

for _ in range(N):
    word = set(list(sys.stdin.readline().strip())) - basic
    for i in word:
        if (i not in basic):
            teach.add(i)
    words.append(word)

if K < 5:
    print(0)
    exit()

if K == 26:
    print(N)
    exit()

if len(teach) < K - 5:
    print(N)
    exit()

for lst in combinations(teach, K-5):
    cnt = 0

    for word in words:
        flag = 0
        for c in word:
            if c not in lst:
                flag = 1
                break
        if flag == 0:
            cnt += 1

    answer = max(answer, cnt)

print(answer)
"""