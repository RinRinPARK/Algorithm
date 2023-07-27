"""
시간초과가 난 코드
permutations로 3개의 벽을 세울 수 있는 모든 경우의 수를 구하고
이를 하나하나 bfs로 탐색하며 해답을 찾는다.

import sys
from itertools import permutations
import copy
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = []
empty = []
viruses = []
ans = 0
for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    graph.append(lst)
    for j in range(M):
        if lst[j] == 0:
            empty.append([i, j])
        elif lst[j] == 2:
            viruses.append([i, j])

candidates = map(list, permutations(empty, 3))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for candidate in candidates:
    map = copy.deepcopy(graph)
    queue = deque()
    result = 0

    for x, y in candidate:
        map[x][y] = 1

    for virus in viruses:
        queue.append(virus)

    while queue:
        m, n = queue.popleft()
        for k in range(4):
            nx = m + dx[k]
            ny = n + dy[k]
            if (0 <= nx < N) and (0 <= ny < M) and (map[nx][ny] == 0):
                map[nx][ny] = 2
                queue.append([nx, ny])

    for arr in map:
        result += arr.count(0)

    ans = max(ans, result)

print(ans)
"""


# 최종 코드
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = []
empty = []
viruses = []
ans = 0
for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    graph.append(lst)
    for j in range(M):
        if lst[j] == 0:
            empty.append([i, j])
        elif lst[j] == 2:
            viruses.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    global ans
    map = [row[:] for row in graph]
    queue = deque(viruses)

    while queue:
        m, n = queue.popleft()
        for k in range(4):
            nx = m + dx[k]
            ny = n + dy[k]
            if (0 <= nx < N) and (0 <= ny < M) and (map[nx][ny] == 0):
                map[nx][ny] = 2
                queue.append([nx, ny])

    count = 0
    for i in range(N):
        for j in range(M):
            if map[i][j] == 0:
                count += 1

    ans = max(ans, count)


def dfs(cnt, start):
    if cnt == 3:
        bfs()
        return

    for i in range(start, len(empty)):
        x, y = empty[i]
        graph[x][y] = 1
        dfs(cnt + 1, i + 1)
        graph[x][y] = 0


dfs(0, 0)
print(ans)
