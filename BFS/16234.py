# python3로 채점 시 시간초과 발생
# pypy3로 채점 시 통과
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
ans = 0
N, L, R = map(int, sys.stdin.readline().split())
A = [[] for _ in range(N)]

for k in range(N):
    A[k] = list(map(int, sys.stdin.readline().split()))

# BFS 아이디어
while True:
    flag0 = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                sum = 0
                history = []
                queue.append([i, j])
                visited[i][j] = 1

                while queue:
                    x, y = queue.popleft()
                    history.append([x, y])
                    sum += A[x][y]
                    for p in range(4):
                        nx = x + dx[p]
                        ny = y + dy[p]

                        if (0 <= nx < N) and (0 <= ny < N) and (L <= abs(A[x][y]-A[nx][ny]) <= R) and (visited[nx][ny] == 0):
                            visited[nx][ny] = 1
                            queue.append([nx, ny])

                if len(history) > 1:
                    flag0 = 1
                    val = sum//len(history)
                    for a, b in history:
                        A[a][b] = val

    if flag0 == 0:
        break
    ans += 1

print(ans)
