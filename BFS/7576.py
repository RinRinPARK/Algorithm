import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
lst = []
queue = deque([])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 0

for _ in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        a, b = queue.popleft()
        for m in range(4):
            if a+dx[m] >= 0 and b+dy[m] >= 0 and a+dx[m] < N and b+dy[m] < M and lst[a+dx[m]][b+dy[m]] == 0:
                lst[a+dx[m]][b+dy[m]] = lst[a][b]+1
                queue.append([a+dx[m], b+dy[m]])


bfs()

for i in lst:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    if max(i) > count:
        count = max(i)

print(count-1)
