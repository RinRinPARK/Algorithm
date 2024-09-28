"""
시간초과 bfs

import sys
from collections import deque

dx = [-1, 1,0,0]
dy = [0, 0,-1,1]
queue = deque()
answer = 0

# 항상 높이가 더 낮은 지점으로만 이동하여 목표 지점까지
# 제일 왼쪽 위 지점에서 출발하여 제일 오른쪽 아래 지점까지 항상 내리막길로만 이동
M, N = map(int, sys.stdin.readline().split())
graph = []
for _ in range(M):
    graph.append(list(map(int, sys.stdin.readline().split())))
queue.append([0,0])

while queue:
    x, y = queue.popleft()

    if [x, y] == [M-1, N-1]:
        answer += 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if (0 <= nx < M) and (0 <= ny < N) and (graph[x][y] > graph[nx][ny]):
            queue.append([nx,ny])


print(answer)
"""
import sys
sys.setrecursionlimit(10 ** 9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):

    if (x, y) == (M-1, N-1):
        return 1
    
    if dp[x][y] == -1:
        
        dp[x][y] = 0

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if (0 <= nx < M) and (0 <= ny < N) and (graph[x][y] > graph[nx][ny]):
                dp[x][y] += dfs(nx, ny)

    return dp[x][y]



M, N = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]
print(dfs(0,0))