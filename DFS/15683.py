# bruteForce + DFS

import sys
import copy

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
modes = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]


def watch(map, mode, x, y):
    for num in mode:
        nx = x + dx[num]
        ny = y + dy[num]
        while (0 <= nx < N) and (0 <= ny < M) and (map[nx][ny] != 6):
            if map[nx][ny] == 0:
                map[nx][ny] = '#'
            nx = nx + dx[num]
            ny = ny + dy[num]


def dfs(depth, graph):

    global ans

    if depth == len(cctv):
        result = 0
        for arr in graph:
            result += arr.count(0)
        ans = min(ans, result)
        return

    curr = copy.deepcopy(graph)
    cam, x, y = cctv[depth]

    for mode in modes[cam]:
        watch(curr, mode, x, y)
        dfs(depth+1, curr)
        curr = copy.deepcopy(graph)


N, M = map(int, sys.stdin.readline().split())
office = []
cctv = []
ans = float("inf")

for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    office.append(lst)
    for j in range(M):
        if lst[j] in [1, 2, 3, 4, 5]:
            cctv.append([lst[j], i, j])

dfs(0, office)
print(ans)
