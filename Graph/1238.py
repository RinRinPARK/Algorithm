import sys
import heapq

# N명의 학생들 중 오고 가는데 가장 오래 걸리는 학생의 소요시간을 출력
N, M, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y, cost = map(int, sys.stdin.readline().split())
    graph[x].append([y, cost])

def dijkstra(start):
    queue = []
    heapq.heappush(queue, [0, start])
    visited = [float("inf") for _ in range(N+1)]
    visited[start] = 0

    while queue:
        v, x = heapq.heappop(queue)

        if visited[x] < v:
            continue

        for node, c in graph[x]:
            if (visited[node] > v + c):
                heapq.heappush(queue, [v + c, node])
                visited[node] = v + c

    return visited

result = 0
for i in range(1, N+1):

    # X까지 이동
    comeout = dijkstra(i)

    # 집까지 다시 이동
    comein = dijkstra(X)

    result = max(result, comeout[X] + comein[i])

print(result)


"""
시간초과

import sys

# N명의 학생들 중 오고 가는데 가장 오래 걸리는 학생의 소요시간을 출력
N, M, X = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    x, y, cost = map(int, sys.stdin.readline().split())
    graph[x][y] = cost

# 각 학생별
# X까지 갈 수 있는 모든 경우의 수를 찾은 후 가장 작은 수 선택
# X에서 N까지 갈 수 있는 모든 경우의 수를 찾은 후 가장 작은 수 선택

def dfs(start, end, visited, dist):
    global answer

    if start == end:
        answer = min(answer, dist)

    for k in range(1, N + 1):
        if (graph[start][k] != 0) and (k not in visited):
            dfs(k, end, visited + [k], dist + graph[start][k])
    return

result = 0
for i in range(1, N+1):

    answer = float("inf")
    dfs(i, X, [i], 0)
    comeout = answer

    answer = float("inf")
    dfs(X, i, [X], 0)
    comein = answer

    result = max(result, comeout + comein)

print(result)
"""