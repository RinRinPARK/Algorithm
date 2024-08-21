import sys
from collections  import deque

# 한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램
# 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N, M = map(int, sys.stdin.readline().split())
queue = deque()
graph = []
for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if lst[j] != 0:
            queue.append([i, j])
    
    graph.append(lst)

ans = 0

while True:
    turn = []
    imsi = []
    ans += 1

    while queue:
        x, y = queue.popleft()
        melt = 0

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if (0<=nx<N) and (0<=ny<M) and (graph[nx][ny] == 0):
                melt += 1

        turn.append([x,y,melt])

    # 한번에 녹이기
    for c,d,e in turn:
        graph[c][d] -= e

        if graph[c][d] < 0: graph[c][d] = 0
        elif graph[c][d] > 0: imsi.append([c,d])

    # 다 녹을때까지 두동강 안나면 or 섬이 이제 없으면
    if len(imsi) == 0:
        print(0)
        break

    # 섬이 두동강 났는지 확인
    visited = [[0 for _ in range(M)] for _ in range(N)]
    check_queue = deque()
    check_queue.append([imsi[0][0], imsi[0][1]])
    island = 0
    visited[imsi[0][0]][imsi[0][1]] = 1

    while check_queue:
        
        m, n = check_queue.popleft()
        island += 1

        for p in range(4):
            nm = m + dx[p]
            nn = n + dy[p]

            if (visited[nm][nn] != 1) and (graph[nm][nn] != 0):
                check_queue.append([nm, nn])
                visited[nm][nn] = 1

    if island < len(imsi):
        print(ans)
        break

    # 아직 하나의 섬이라면 다시 턴 시작
    for a, b in imsi:
        queue.append([a, b])
