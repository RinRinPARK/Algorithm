import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()

M, N = map(int, sys.stdin.readline().split())
visited = [[-1 for _ in range(M)] for _ in range(N)]
maze = []
for _ in range(N):
    maze.append(list(sys.stdin.readline().strip()))
visited[0][0] = 0
queue.append([0,0])

while queue:
    x, y = queue.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if (0 <= nx < N) and (0 <= ny < M) and (visited[nx][ny] == -1):
            if int(maze[nx][ny]) == 0:
                visited[nx][ny] = visited[x][y]
                # 0인 방을 우선적으로 방문하게끔 appendleft로 넣어줌.
                queue.appendleft([nx,ny])
            else:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])

print(visited[N-1][M-1])
