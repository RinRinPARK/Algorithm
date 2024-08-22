import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1

for x in range(N):
    for y in range(N):
        k = graph[x][y]

        if (k == 0) or (dp[x][y] == 0):
            continue

        nx = x + k
        ny = y + k

        if (0 <= nx < N):
            dp[nx][y] += dp[x][y]
        if (0 <= ny < N):
            dp[x][ny] += dp[x][y]


print(dp[N-1][N-1])


"""

메모리 초과 난 코드

queue = deque()
queue.append([0,0])

while queue:
    x, y = queue.popleft()

    if (x, y) == (N-1, N-1):
        graph[x][y] += 1
        continue

    num = graph[x][y]

    nx = x + num
    ny = y + num

    if (0 <= nx < N) :
        queue.append([nx, y])
    if (0 <= ny < N):
        queue.append([x, ny])

print(graph[N-1][N-1])

"""
