import sys

N, K = map(int, sys.stdin.readline().split())
things = [[0, 0]]
tot_val = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
    things.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = things[i][0]
        value = things[i][1]

        if j < weight:
            tot_val[i][j] = tot_val[i-1][j]
        else:
            tot_val[i][j] = max(tot_val[i-1][j], value+tot_val[i-1][j-weight])

print(tot_val[N][K])
