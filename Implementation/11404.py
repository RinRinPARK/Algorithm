import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[float("inf") for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)

for m in range(1, N+1):
    for n in range(1, N+1):
        for k in range(1, N+1): 
            graph[m][n] = min(graph[m][n], graph[m][k]+graph[k][n])


# i 도시에서 j 도시로 가는데 필요한 최소 비용 출력
for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == float("inf"):
            print(0, end=" ")
            continue

        print(graph[i][j], end= " ")

    print()
        

