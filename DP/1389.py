import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[float("inf") for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A][B] = 1
    graph[B][A] = 1

for k in range(1, N+1):
    for m in range(1, N+1):
        for n in range(1, N+1):
            graph[m][n] = min(graph[m][n], graph[m][k] + graph[k][n])

lst = []
for i in range(1, N+1):
    result = 0
    for j in range(1, N+1):
        if graph[i][j] != float("inf"):
            result += graph[i][j]
    lst.append(result)

print(lst.index(min(lst))+1)