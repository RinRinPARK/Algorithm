import sys
import math


def move(graph, balls):
    curr_graph = [[[] for _ in range(N+1)] for _ in range(N+1)]
    curr_balls = []

    while balls:
        r, c, m, s, d = balls.pop()
        nr = (r + dy[d]*s) % N + 1
        nc = (c+dx[d]*s) % N + 1
        curr_graph[nr][nc].append([m, s, d])

    for i in range(1, N+1):
        for j in range(1, N+1):
            if (len(curr_graph[i][j]) != 0):
                if (len(curr_graph[i][j]) == 1):
                    curr_balls.append(
                        [i, j, curr_graph[i][j][0][0], curr_graph[i][j][0][1], curr_graph[i][j][0][2]])
                else:
                    new_m = 0
                    new_s = 0
                    count = 0
                    odd = 0
                    even = 0
                    for k in range(len(curr_graph[i][j])):
                        x, y, d = curr_graph[i][j].pop()
                        new_m += x
                        new_s += y
                        count += 1
                        if (d % 2) == 0:
                            even += 1
                        else:
                            odd += 1

                    new_m = math.trunc(new_m/5)
                    new_s = math.trunc(new_s/count)

                    if new_m == 0:
                        continue

                    if (even != count) and (odd != count):
                        for d in range(1, 8, 2):
                            curr_graph[i][j].append([new_m, new_s, d])
                            curr_balls.append([i, j, new_m, new_s, d])
                    else:
                        for d in range(0, 7, 2):
                            curr_graph[i][j].append([new_m, new_s, d])
                            curr_balls.append([i, j, new_m, new_s, d])

    return curr_graph, curr_balls


dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
N, M, K = map(int, sys.stdin.readline().split())
graph = [[[] for _ in range(N+1)] for _ in range(N+1)]
balls = []
for _ in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    graph[r][c].append([m, s, d])
    balls.append([r, c, m, s, d])

for i in range(K):
    graph, balls = move(graph, balls)

ans = 0
for m in range(len(balls)):
    ans += balls[m][2]

print(ans)
