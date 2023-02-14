import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
lst = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    lst[B].append(A)


def bfs(i):
    global count
    queue = deque([i])
    visited[i] = 1
    count += 1
    while queue:
        a = queue.popleft()
        for j in lst[a]:
            if visited[j] == 0:
                visited[j] = 1
                queue.append(j)
                count += 1


result = [0]
for i in range(1, N+1):
    visited = [0 for _ in range(N+1)]
    count = 0
    bfs(i)
    result.append(count)

a = max(result)
for j in range(1, N+1):
    if result[j] == a:
        print(j, end=" ")
