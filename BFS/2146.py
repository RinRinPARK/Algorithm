import sys
from collections import deque

# 지도가 주어질 때, 가장 짧은 다리 하나를 놓아 두 대륙을 연결하는 방법
dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = float("inf")

# 섬 구분해주기
visited = [[0 for _ in range(N)] for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            visited[i][j] = 1

            if graph[i][j] == 1:
                cnt += 1
                queue = deque()
                queue.append([i,j])

                while queue:
                    x, y = queue.popleft()
                    graph[x][y] = cnt

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if (0 <= nx < N) and (0 <= ny < N) and (visited[nx][ny] == 0) and (graph[nx][ny] == 1):
                            visited[nx][ny] = 1
                            queue.append([nx,ny])

# 가장 작은 거리 찾기
for i in range(N):
    for j in range(N):

        if graph[i][j] != 0:
            island = graph[i][j]
            q = deque()

            for p in range(4):
                    nm = i + dx[p]
                    nn = j + dy[p]
                    
                    if (0 <= nm < N) and (0 <= nn < N):
                        if (graph[nm][nn] == 0):
                            q.append([nm, nn, 1])

            if len(q) == 0:
                continue

            visit = [[float("inf") for _ in range(N)] for _ in range(N)]
            while q:
                w, v, val = q.popleft()

                for p in range(4):
                    nw = w + dx[p]
                    nv = v + dy[p]
                    
                    if (0 <= nw < N) and (0 <= nv < N) and (visit[nw][nv] > val+1):
                        if (graph[nw][nv] == 0):
                            visit[nw][nv] = val + 1
                            q.append([nw, nv, val + 1])
                        elif (graph[nw][nv] != 0) and (graph[nw][nv] != island):
                            answer = min(answer, val)

print(answer)