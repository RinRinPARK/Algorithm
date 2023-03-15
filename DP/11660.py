import sys
N, M = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(N+1)]]
lst = []
sums = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(N):
    val = list(map(int, sys.stdin.readline().split()))
    val.insert(0, 0)
    graph.append(val)
for _ in range(M):
    lst.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N+1):
    for j in range(1, N+1):
        sums[i][j] = sums[i-1][j]+sums[i][j-1]-sums[i-1][j-1]+graph[i][j]

for element in lst:
    x1 = element[0]
    y1 = element[1]
    x2 = element[2]
    y2 = element[3]
    print(sums[x2][y2]-(sums[x2][y1-1]+sums[x1-1][y2])+sums[x1-1][y1-1])
