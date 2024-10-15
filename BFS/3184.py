import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, sys.stdin.readline().split())
board = []
for i in range(R):
    board.append(list(sys.stdin.readline().strip()))

visited = [[0 for _ in range(C)] for _ in range(R)]

cnt = 1
ans_sheep = 0
ans_wolf = 0
for i in range(R):
    for j in range(C):
        if (visited[i][j] == 0) and (board[i][j] != '#'):
            queue = deque()

            sheep = 0
            wolf = 0

            if (board[i][j] == 'v'):
                wolf += 1
            elif (board[i][j] == 'o'):
                sheep += 1

            queue.append([i, j])
            visited[i][j] = cnt

            while queue:
                x, y = queue.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if (0 <= nx < R) and (0 <= ny < C) and (visited[nx][ny] == 0) and (board[nx][ny] != '#'):
                        if (board[nx][ny] == 'v'):
                            wolf += 1
                        elif (board[nx][ny] == 'o'):
                            sheep += 1
                    
                        visited[nx][ny] = cnt
                        queue.append([nx, ny])
            if wolf >= sheep:
                ans_wolf += wolf
            else:
                ans_sheep += sheep

            cnt += 1

print(ans_sheep, ans_wolf)
