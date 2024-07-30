# 공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간
# 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수

import sys
from collections import deque
 
r, c = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
results = []
time = 0 
 
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
 
def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    cnt = 0
 
    while q:
        x, y = q.popleft()
 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    cnt += 1
                visited[nx][ny] = True
    results.append(cnt)
    return cnt
 
while True:
    visited = [[False] * c for _ in range(r)]
 
    cnt = bfs()
 
    if cnt == 0:
        print(time)
        print(results[-2])
        break
    time += 1