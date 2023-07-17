import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
graph = []
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
queue = deque()
zero = 0

for h in range(H):
    lst = []
    for j in range(N):
        inpt = list(map(int, sys.stdin.readline().split()))
        for i in range(len(inpt)):
            if inpt[i] == 1:
                queue.append([h, j, i])
            elif inpt[i] == 0:
                zero = 1
        lst.append(inpt)
    graph.append(lst)

if zero == 0:
    print(0)
    exit(0)

while queue:
    x, y, z = queue.popleft()
    for k in range(6):
        nx = x + dx[k]
        ny = y + dy[k]
        nz = z + dz[k]

        if (0 <= nx < H) and (0 <= ny < N) and (0 <= nz < M) and (graph[nx][ny][nz] == 0):
            graph[nx][ny][nz] = graph[x][y][z] + 1
            queue.append([nx, ny, nz])


result = 0
for m in range(H):
    for n in range(N):
        if result < max(graph[m][n]):
            result = max(graph[m][n])
        if 0 in graph[m][n]:
            print(-1)
            exit(0)

print(result - 1)
