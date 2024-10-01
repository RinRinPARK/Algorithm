import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 외부 공기를 BFS로 탐색하여 치즈와 접촉하는 공기를 찾는다.
def bfs_outside_air():
    queue = deque()
    queue.append((0, 0))  # 시작점을 외부 공기로 간주 (가장자리는 항상 공기)
    visited[0][0] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                # 치즈가 아닌 빈 공간이면 외부 공기로 간주
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                # 치즈라면 외부 공기와 접촉하는 치즈로 표시
                elif graph[nx][ny] == 1:
                    melt_list[nx][ny] += 1

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = 0
while True:
    visited = [[False] * M for _ in range(N)]
    melt_list = [[0] * M for _ in range(N)]  # 치즈가 녹는지 기록할 리스트

    # 외부 공기를 탐색
    bfs_outside_air()

    # 녹을 치즈를 찾아서 녹임
    melt_flag = False
    for i in range(N):
        for j in range(M):
            # 외부 공기와 2면 이상 접촉한 치즈는 녹는다
            if graph[i][j] == 1 and melt_list[i][j] >= 2:
                graph[i][j] = 0
                melt_flag = True

    # 치즈가 모두 녹았으면 종료
    if not melt_flag:
        break

    answer += 1  # 시간이 1시간 경과

print(answer)
