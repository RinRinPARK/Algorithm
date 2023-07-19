import sys
from collections import deque

# 정보 입력 받기
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
graph = [[0 for _ in range(N)] for _ in range(N)]
direction = []

for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = 1
L = int(sys.stdin.readline())

for _ in range(L):
    num, drct = sys.stdin.readline().split()
    direction.append([int(num), drct])

count = 0
way = direction.pop(0)
heading = 2  # 방향
tail = deque()
tail.append([0, 0])
head = [0, 0]
# 게임 시작
while True:
    count += 1
    # 이동먼저
    if heading == 1:
        head[0] -= 1
    elif heading == 2:
        head[1] += 1
    elif heading == 3:
        head[0] += 1
    else:
        head[1] -= 1

    x, y = head[0], head[1]

    # 부딪히면 while문 탈출 후 count 반환
    if (x < 0) or (x >= N) or (y < 0) or (y >= N):
        break

    # 자기 자신에게 부딪히면 탈출
    if graph[x][y] == 2:
        break

    # 이동
    if graph[x][y] == 0:
        graph[x][y] = 2
        tail.append([x, y])
        tx, ty = tail.popleft()
        graph[tx][ty] = 0

    # 사과먹기
    if graph[x][y] == 1:
        graph[x][y] = 2
        tail.append([x, y])

    # 방향전환
    if count == way[0]:
        if heading == 1:
            if way[1] == 'D':
                heading = 2
            else:
                heading = 4
        elif heading == 2:
            if way[1] == 'D':
                heading = 3
            else:
                heading = 1
        elif heading == 3:
            if way[1] == 'D':
                heading = 4
            else:
                heading = 2
        else:
            if way[1] == 'D':
                heading = 1
            else:
                heading = 3
        if len(direction) > 0:
            way = direction.pop(0)
        else:
            way = [0, 0]

print(count)
