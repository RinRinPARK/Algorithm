import sys

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 가로, 세로, 대각선
dp = [[[0,0,0] for _ in range(N)] for _ in range(N)]

# 0번째 행의 가로 가능 수는 1
for i in range(1, N):
    if graph[0][i] != 1:
        dp[0][i][0] = 1
    else:
        break

for a in range(1, N):
    for b in range(1, N):
        if graph[a][b] != 1:

            # 가로
            if (0<= b-1 < N):
                dp[a][b][0] = dp[a][b-1][0] + dp[a][b-1][2]

            # 세로
            if (0<= a-1 < N):
                dp[a][b][1] = dp[a-1][b][1] + dp[a-1][b][2]

            # 대각선
            if (0<= a-1 < N) and (0<= b-1 < N) and (graph[a-1][b] != 1) and (graph[a][b-1] != 1):
                dp[a][b][2] = dp[a-1][b-1][0] + dp[a-1][b-1][1] + dp[a-1][b-1][2]

print(sum(dp[N-1][N-1]))


"""
시간초과 bfs

import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dr = [[0,1,0,1], [1,1,0,1]]
dh = [[1,0,1,0], [1,1,1,0]]
dd = [[0,1,1,1], [1,0,1,1], [1,1,1,1]]

queue = deque()
# [첫번째y좌표, 첫번째x, 두번째y, 두번째x, 놓여있는방향(0:가로, 1: 세로, -1: 대각선)]
queue.append([0,1,0,0,0])
result = 0

while queue:
    fy,fx,sy,sx,d = queue.popleft()

    if ((fy, fx) == (N-1, N-1)) or ((sy, sx) == (N-1, N-1)):
        result += 1

    if d == 0:
        for i in range(2):
            nfy = fy + dr[i][0]
            nfx = fx + dr[i][1]
            nsy = sy + dr[i][2]
            nsx = sx + dr[i][3]

            if (nfy < N and nfx < N and nsy < N and nsx < N) and (graph[nfy][nfx] != 1) and (graph[nsy][nsx] != 1):
                if i == 0:
                    queue.append([nfy, nfx, nsy, nsx, 0])
                elif (i == 1) and (graph[nfy][nfx-1] != 1) and (graph[nfy-1][nfx] != 1):
                    queue.append([nfy, nfx, nsy, nsx, -1])

    elif d == 1:
        for i in range(2):
            nfy = fy + dh[i][0]
            nfx = fx + dh[i][1]
            nsy = sy + dh[i][2]
            nsx = sx + dh[i][3]

            if (nfy < N and nfx < N and nsy < N and nsx < N) and (graph[nfy][nfx] != 1) and (graph[nsy][nsx] != 1):
                if i == 0:
                    queue.append([nfy, nfx, nsy, nsx, 1])
                elif (i == 1) and (graph[nfy][nfx-1] != 1) and (graph[nfy-1][nfx] != 1):
                    queue.append([nfy, nfx, nsy, nsx, -1])

    else:
        for i in range(3):
            nfy = fy + dd[i][0]
            nfx = fx + dd[i][1]
            nsy = sy + dd[i][2]
            nsx = sx + dd[i][3]

            if (nfy < N and nfx < N and nsy < N and nsx < N) and (graph[nfy][nfx] != 1) and (graph[nsy][nsx] != 1):
                if i == 0:
                    queue.append([nfy, nfx, nsy, nsx, 0])
                elif i == 1:
                    queue.append([nfy, nfx, nsy, nsx, 1])
                elif (i == 2) and (graph[nfy][nfx-1] != 1) and (graph[nfy-1][nfx] != 1):
                    queue.append([nfy, nfx, nsy, nsx, -1])



print(result)
"""