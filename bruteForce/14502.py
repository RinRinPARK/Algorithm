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
