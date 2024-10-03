import sys
import heapq

# 잃는 금액을 최소로 하여 동굴 건너편까지 이동해야 하며, 
# 한 번에 상하좌우 인접한 곳으로 1칸씩 이동

# 링크가 잃을 수밖에 없는 최소 금액은 얼마

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(sys.stdin.readline())
game = 1
while N != 0:
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    queue = []
    heapq.heappush(queue, [graph[0][0], 0, 0])
    visited = [[float("inf") for _ in range(N)] for _ in range(N)]

    while queue:
        cnt, x, y = heapq.heappop(queue)

        if (x, y) == (N-1, N-1):
            print("Problem ", game, ": ", cnt, sep = '')
            N = int(sys.stdin.readline())
            game += 1
            break

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if (0 <= nx < N) and (0 <= ny < N) and (visited[nx][ny] > cnt + graph[nx][ny]):
                heapq.heappush(queue, [cnt + graph[nx][ny], nx, ny])
                visited[nx][ny] = cnt + graph[nx][ny]


"""
시간 초과 BFS 코드

import sys
from collections import deque

# 잃는 금액을 최소로 하여 동굴 건너편까지 이동해야 하며, 
# 한 번에 상하좌우 인접한 곳으로 1칸씩 이동

# 링크가 잃을 수밖에 없는 최소 금액은 얼마

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(sys.stdin.readline())
game = 1
while N != 0:
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    queue = deque()
    queue.append([0, 0, graph[0][0]])
    answer = float("inf")
    visited = [[float("inf") for _ in range(N)] for _ in range(N)]

    while queue:
        x, y, cnt = queue.popleft()

        if cnt > answer:
            continue

        if (x, y) == (N-1, N-1):
            answer = min(answer, cnt)
            continue

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if (0 <= nx < N) and (0 <= ny < N) and (visited[nx][ny] > cnt + graph[nx][ny]):
                queue.append([nx, ny, cnt + graph[nx][ny]])
                visited[nx][ny] = cnt + graph[nx][ny]

    print("Problem ", game, ": ", answer, sep = '')
    N = int(sys.stdin.readline())
    game += 1

"""