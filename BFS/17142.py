# bruteForce + BFS

import sys
from collections import deque
from itertools import combinations
import copy


def BFS(arr, curr, viruses):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque()
    count = 0
    for ele in arr:
        queue.append(ele)
    while queue:
        x, y, d = queue.popleft()
        visited[x][y] = 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if (0 <= nx < N) and (0 <= ny < N) and (visited[nx][ny] == 0) and (curr[nx][ny] != 1):
                visited[nx][ny] = 1
                if (curr[nx][ny] == 0):
                    curr[nx][ny] = 2
                    count = d + 1
                queue.append([nx, ny, d+1])

    for i in range(N):
        for j in range(N):
            if (curr[i][j] == 0):
                return -1

    return count


N, M = map(int, sys.stdin.readline().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = []
viruses = []
for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    graph.append(lst)
    for j in range(N):
        if lst[j] == 2:
            viruses.append([i, j, 0])

combi = list(combinations(viruses, M))

ans = float("inf")
for arr in combi:
    curr = copy.deepcopy(graph)
    val = BFS(arr, curr, viruses)
    if val != -1:
        ans = min(ans, val)

if ans != float("inf"):
    print(ans)
else:
    print(-1)
