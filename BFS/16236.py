import sys
from collections import deque


def BFS():
    queue = deque()
    queue.append(loc)
    curr = [[-1 for _ in range(N)] for _ in range(N)]
    curr[loc[0]][loc[1]] = 0
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if (0 <= nx < N) and (0 <= ny < N) and (curr[nx][ny] == -1) and (graph[nx][ny] <= size):
                curr[nx][ny] = curr[x][y] + 1
                queue.append([nx, ny])

    return curr


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(sys.stdin.readline())
graph = []
size = 2
loc = [0, 0]

for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    graph.append(lst)
    for j in range(N):
        if lst[j] == 9:
            loc = [i, j]
            graph[i][j] = 0

ans = 0
ate = 0
while True:

    dists = BFS()
    location = []
    dist = float("inf")

    # 물고기 먹기
    for i in range(N):
        for j in range(N):
            if (dists[i][j] != -1) and (0 < graph[i][j] < size):
                if (dists[i][j] < dist):
                    dist = dists[i][j]
                    location = [i, j]

    # 먹을 물고기가 없을 때
    if (dist == float("inf")):
        break

    ans += dist

    # 자신의 크기와 같은 수의 물고기를 먹으면 크기 1 증가
    if (size <= ate + 1):
        ate = 0
        size += 1
        loc = [location[0], location[1]]
        graph[loc[0]][loc[1]] = 0
    else:
        ate += 1
        loc = [location[0], location[1]]
        graph[loc[0]][loc[1]] = 0

print(ans)
