import sys
import heapq

# 지훈이의 위치와 불이 붙은 위치를 감안해서 지훈이가 불에 타기전에 탈출할 수 있는지의 여부, 
# 그리고 얼마나 빨리 탈출할 수 있는지를 결정

# 미로를 탈출 할 수 없는 경우 IMPOSSIBLE 을 출력
# 미로를 탈출할 수 있는 경우에는 가장 빠른 탈출시간을 출력
dx = [-1,1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, sys.stdin.readline().split())
graph = []

queuej = []
queuef = []
visited = [[float("inf") for _ in range(C)] for _ in range(C)]
 
for i in range(R):
    lst = list(sys.stdin.readline().strip())
    for j in range(C):
        if lst[j] == 'J':
            heapq.heappush(queuej, [0, [i, j]])
            visited[i][j] = 0
            lst[j] = '.'
        elif lst[j] == 'F':
            heapq.heappush(queuef, [i, j])
    graph.append(lst)

# 불 먼저 확산, 지훈 이동

while True:
    fire = []
    while queuef:
        fx, fy = heapq.heappop(queuef)

        for k in range(4):
            nfx = fx + dx[k]
            nfy = fy + dy[k]

            if (0 <= nfx < R) and (0 <= nfy < C) and (graph[nfx][nfy] == '.'):
                graph[nfx][nfy] = 'F'
                fire.append([nfx, nfy])
    jihoon = []
    while queuej:
        cnt, jlst = heapq.heappop(queuej)
        jx = jlst[0]
        jy = jlst[1]

        for k in range(4):
            njx = jx + dx[k]
            njy = jy + dy[k]

            if not ((0 <= njx < R) and (0 <= njy < C)):
                print(cnt + 1)
                exit()

            if (0 <= njx < R) and (0 <= njy < C) and (graph[njx][njy] == '.') and (visited[njx][njy] > cnt + 1):
                visited[njx][njy] = cnt + 1
                jihoon.append([cnt + 1, [njx, njy]])

    if (len(fire) == 0) and (len(jihoon) == 0):
        print("IMPOSSIBLE")
        exit()

    for fir in fire:
        heapq.heappush(queuef, fir)


    for j in jihoon:
        heapq.heappush(queuej, j)
    
