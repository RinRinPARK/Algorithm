import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
result = [0]*(N+1)

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
queue = deque()
queue.append(1)
visited[1] = 1


def bfs():
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = 1
                result[i] = x
                queue.append(i)


bfs()

for i in range(2, N+1):
    print(result[i])
