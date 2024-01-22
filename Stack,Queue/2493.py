"""
시간초과 난 코드

import sys

N = int(sys.stdin.readline())
tops = list(map(int, sys.stdin.readline().split()))
result = [0]

for i in range(1, N):
    flag = 0
    for j in range(i-1, -1, -1):
        if tops[j] >= tops[i]:
            result.append(j+1)
            flag = 1
            break
    if flag == 0:
        result.append(0)

print(*result)
"""

import sys

N = int(sys.stdin.readline())
tops = list(map(int, sys.stdin.readline().split()))
result = [0]
stack = [[tops[0], 1]]

for i in range(1, N):
    while stack and stack[-1][0] < tops[i]:
        stack.pop()

    if stack:
        result.append(stack[-1][1])
    else:
        result.append(0)
    stack.append([tops[i], i+1])

print(*result)
