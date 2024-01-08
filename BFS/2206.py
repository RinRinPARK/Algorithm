import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, sys.stdin.readline().split())
visited = [[[0,0] for _ in range(M)] for _ in range(N)]
graph = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))

queue = deque()
# [x좌표, y좌표, 남은 벽 부수기 가능 횟수(최대 1)] 
queue.append([0, 0, 0])
visited[0][0][0] = 1

while queue:
    x, y, cnt = queue.popleft()

    if (x == N - 1) and (y == M - 1):
        print(visited[x][y][cnt])
        exit(0)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M):
            # 다음이 벽이고 벽을 아직 하나도 안부순 경우
            if (graph[nx][ny] == 1) and (cnt == 0):
                queue.append([nx, ny, cnt + 1])
                visited[nx][ny][1] = visited[x][y][0] + 1

            # 다음이 이동 가능한 칸인 경우
            if (graph[nx][ny] == 0) and (visited[nx][ny][cnt] == 0):
                queue.append([nx, ny, cnt])
                visited[nx][ny][cnt] = visited[x][y][cnt] + 1

print(-1)