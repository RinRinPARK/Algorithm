import sys
n = int(sys.stdin.readline())
x, y = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
result = []


def dfs(num, count):
    visited[num] = 1
    if num == y:
        result.append(count)
    for i in graph[num]:
        if visited[i] == 0:
            dfs(i, count+1)


for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited[x] = 1
dfs(x, 0)

if len(result) == 0:
    print(-1)
else:
    print(result[0])
