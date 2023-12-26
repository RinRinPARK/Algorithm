import sys
import heapq
"""
메모리 초과 코드

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
dist = [float("inf") for _ in range(V+1)]
for _ in range(E):
    u,v,m = map(int ,sys.stdin.readline().split())
    graph[u][v] = m

# 최단 경로 찾는 로직
def DFS(num, dest, value):
    if num == dest:
        dist[num] = min(dist[num], value)
    else:
        for j in range(1, V+1):
            if graph[num][j] != 0:
                DFS(j, dest, value + graph[num][j])

# 최단 경로 출력
for i in range(1, V+1):
    if i != K:
        DFS(1, i, 0)
    else:
        dist[i] = 0

for k in range(1, V+1):
    if dist[k] != float("inf"):
        print(dist[k])
    else:
        print("INF")

"""

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]
dist = [float("inf") for _ in range(V+1)]
visited = [0 for _ in range(V+1)]
for _ in range(E):
    u,v,m = map(int ,sys.stdin.readline().split())
    graph[u].append([v,m])

heap = []
heapq.heappush(heap, (0, K))
dist[K] = 0

# 최단경로 찾기
while heap:
    dis, node = heapq.heappop(heap)

    if visited[node] == 1:
        continue

    visited[node] = 1
    for vertex, val in graph[node]:
        new = dis + val

        if new < dist[vertex]:
            dist[vertex] = new
            heapq.heappush(heap, (new, vertex))

# 최단 경로 출력
for k in range(1, V+1):
    if dist[k] != float("inf"):
        print(dist[k])
    else:
        print("INF")