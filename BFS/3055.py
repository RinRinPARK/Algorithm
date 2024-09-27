import sys
from collections import deque

# 물이 있는 칸과 인접해있는 비어있는 칸(적어도 한 변을 공유)은 물이 차게 된다
# 물과 고슴도치는 돌을 통과할 수 없다
# 고슴도치는 물로 차있는 구역으로 이동할 수 없고, 물도 비버의 소굴로 이동할 수 없다

# 고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, sys.stdin.readline().split())
graph = []
water_queue = deque()
dochi_queue = deque()

for i in range(R):
    row = list(sys.stdin.readline().strip())
    for j in range(C):
        if row[j] == 'S':
            dochi_queue.append((i, j, 0))
            row[j] = '.'
        elif row[j] == '*':
            water_queue.append((i, j))
    graph.append(row)

# 고슴도치 방문 여부
dochi_visited = [[False] * C for _ in range(R)]
dochi_visited[dochi_queue[0][0]][dochi_queue[0][1]] = True

while dochi_queue:
    # 물 먼저 확장
    for _ in range(len(water_queue)):
        wx, wy = water_queue.popleft()
        for k in range(4):
            nx = wx + dx[k]
            ny = wy + dy[k]
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == '.':
                graph[nx][ny] = '*'
                water_queue.append((nx, ny))

    # 고슴도치 이동
    for _ in range(len(dochi_queue)):
        x, y, t = dochi_queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == 'D':
                    print(t + 1)
                    sys.exit(0)

                if graph[nx][ny] == '.' and not dochi_visited[nx][ny]:
                    dochi_visited[nx][ny] = True
                    dochi_queue.append((nx, ny, t + 1))

print("KAKTUS")

