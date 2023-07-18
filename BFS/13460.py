import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = []
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
visited = []

for i in range(N):
    inpt = list(sys.stdin.readline().rstrip())
    graph.append(inpt)
    if 'R' in inpt:
        r = [i, inpt.index('R')]
    if 'B' in inpt:
        b = [i, inpt.index('B')]

queue.append(r+b)
visited.append(r+b)

while queue:
    for _ in range(len(queue)):
        rx, ry, bx, by = queue.popleft()

        if result > 10:
            print(-1)
            exit(0)

        if graph[rx][ry] == 'O':
            print(result)
            exit(0)

        # 올 수 있는 것: # O .
        for i in range(4):
            nrx, nry = rx, ry
            nbx, nby = bx, by
            while True:
                nrx += dx[i]
                nry += dy[i]
                if graph[nrx][nry] == '#':
                    nrx -= dx[i]
                    nry -= dy[i]
                    break
                if (graph[nrx][nry] == 'O'):
                    break
            while True:
                nbx += dx[i]
                nby += dy[i]
                if graph[nbx][nby] == '#':
                    nbx -= dx[i]
                    nby -= dy[i]
                    break
                if (graph[nbx][nby] == 'O'):
                    break
            if (graph[nbx][nby] == 'O'):
                continue
            if (nrx == nbx) and (nry == nby):
                if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if [nrx, nry, nbx, nby] not in visited:
                queue.append([nrx, nry, nbx, nby])
                visited.append([nrx, nry, nbx, nby])

    result += 1
print(-1)
