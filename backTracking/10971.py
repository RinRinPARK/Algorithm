#TSP

import sys

N = int(sys.stdin.readline())
W = []
for _ in range(N):
    W.append(list(map(int, sys.stdin.readline().split())))

visited = [[0 for _ in range(N)] for _ in range(N)]
city = [0 for _ in range(N)]
city[0] = 1
result = float("inf")

def dfs(x, y, v):
    global result


    # 모든 city를 다 돌았고, 마지막 city에서 가장 처음 city로 돌아갈 수 있을 때
    if (sum(city) == N) and (W[y][0] != 0):
        result = min(result, v+W[y][0])

    for k in range(N):
        if (W[y][k] != 0) and (city[k] == 0):
            city[k] = 1
            dfs(y, k, v+W[y][k])
            city[k] = 0

dfs(0,0,0)

print(result)