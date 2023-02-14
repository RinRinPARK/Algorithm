import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())
queue = deque([S])
visited = [0 for _ in range(F+1)]


def bfs():
    visited[S] = 1
    while queue:
        x = queue.popleft()
        if x == G:
            print(visited[G]-1)
            queue.clear()
        ux = x+U
        dx = x-D
        if 0 < ux <= F and visited[ux] == 0:
            visited[ux] = visited[x]+1
            queue.append(ux)
        if 0 < dx <= F and visited[dx] == 0:
            visited[dx] = visited[x]+1
            queue.append(dx)
    if visited[G] == 0:
        print("use the stairs")


bfs()
