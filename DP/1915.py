import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    lst = list(sys.stdin.readline().strip())
    for i in range(m):
        lst[i] = int(lst[i])
    graph.append(lst)

dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0] = graph[0]
for k in range(n):
    dp[k][0] = graph[k][0]
for i in range(1, n):
    for j in range(1, m):
        if graph[i][j] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

ans = 0
for m in dp:
    ans = max(ans, max(m))
print(ans**2)