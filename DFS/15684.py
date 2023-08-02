# DFS + BruteForce
# pypy3로는 정답이지만 python3로 채점시 시간 초과

import sys


def move(graph, N, H):
    for i in range(1, N+1):
        now = i
        for j in range(1, H+1):
            if graph[j][now-1]:
                now -= 1
            elif graph[j][now]:
                now += 1
        if now != i:
            return False
    return True


def dfs(depth, graph, N, H, num):
    global ans

    if depth >= ans:
        return

    if (move(graph, N, H)):
        ans = depth
        return

    # "줄 하나 그려보고, 따라서 가보고" 반복
    for c in range(num, len(combi)):
        x, y = combi[c]
        if not graph[x][y-1] and not graph[x][y+1]:
            graph[x][y] = 1
            dfs(depth+1, graph, N, H, c+1)
            graph[x][y] = 0


N, M, H = map(int, sys.stdin.readline().split())
width = [[0 for _ in range(N+1)] for _ in range(H+1)]
ans = 4
combi = []

if M == 0:
    print(0)
    exit(0)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    width[a][b] = 1

for i in range(1, H+1):
    for j in range(1, N):
        if not width[i][j-1] and not width[i][j] and not width[i][j+1]:
            combi.append([i, j])
dfs(0, width, N, H, 0)

if ans <= 3:
    print(ans)
else:
    print(-1)
