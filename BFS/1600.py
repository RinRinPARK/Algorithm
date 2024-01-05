import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
hx = [-1, -2, -2, -1, 1, 2, 2, 1]
hy = [-2, -1, 1, 2, -2, -1, 1, 2]
result = float("inf")

K = int(sys.stdin.readline())
graph = []
W, H = map(int, sys.stdin.readline().split())
for _ in range(H):
    graph.append(list(map(int, sys.stdin.readline().split())))
queue = deque()
# x좌표, y좌표, 남은 말 움직임 이동수, 총 이동 수
queue.append([0, 0, K, 0])
visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]

while queue:
    x, y, cnt, mv = queue.popleft()

    if (x == H - 1) and (y == W - 1):
        result = min(result, mv)
        continue

    if cnt > 0:
        for i in range(8):
            hnx = x + hx[i]
            hny = y + hy[i]
            if (0 <= hnx < H) and (0 <= hny < W) and (visited[hnx][hny][cnt - 1] == 0) and (graph[hnx][hny] == 0):
                queue.append([hnx, hny, cnt - 1, mv + 1])
                visited[hnx][hny][cnt - 1] = 1

    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        if (0 <= nx < H) and (0 <= ny < W) and (visited[nx][ny][cnt] == 0) and (graph[nx][ny] == 0):
            queue.append([nx, ny, cnt, mv + 1])
            visited[nx][ny][cnt] = 1

if result == float("inf"):
    print(-1)
else:
    print(result)