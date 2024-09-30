import sys

N, M = map(int, sys.stdin.readline().split())
candy = []
for _ in range(N):
    candy.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = candy[0][0]
for k in range(1, M):
    dp[0][k] = dp[0][k-1] + candy[0][k]
for p in range(1, N):
    dp[p][0] = dp[p-1][0] + candy[p][0]

for i in range(1, N):
    for j in range(1, M):

        a = candy[i][j] + dp[i-1][j]
        b = candy[i][j] + dp[i][j-1]
        c = candy[i][j] + dp[i-1][j-1]
        dp[i][j] = max([a,b,c])

print(dp[N-1][M-1])

"""
메모리 초과 BFS코드


import sys
from collections import deque

# 준규가 (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수의 최댓값
dx = [1, 0, 1]
dy = [0, 1, 1]

N, M = map(int, sys.stdin.readline().split())
candy = []
for _ in range(N):
    candy.append(list(map(int, sys.stdin.readline().split())))
queue = deque()
queue.append([0,0,candy[0][0]])
answer = 0

while queue:
    x, y, v = queue.popleft()

    if (x, y) == (N-1, M-1):
        answer = max(answer, v)
        continue

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M):
            queue.append([nx,ny,v+candy[nx][ny]])

print(answer)
"""