import sys


def turn():
    global d

    if d == 0:
        d = 3
    elif d == 1:
        d = 0
    elif d == 2:
        d = 1
    else:
        d = 2


N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
graph = []
count = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

while True:
    blank = 0

    # 현재 칸이 아직 청소되어 있지 않은 경우엔 청소
    if graph[r][c] == 0:
        graph[r][c] = 2
        count += 1

    # 현재 칸의 주변 4칸 중 청소되지 않은 칸이 있는지 확인
    for i in range(4):
        nx = r + dy[i]
        ny = c + dx[i]
        if (0 <= nx < N) and (0 <= ny < M) and (graph[nx][ny] == 0):
            blank = 1
            break

    # 청소되지 않은 칸이 있는 경우
    if blank == 1:
        # 1. 반시계 방향으로 90도 회전
        turn()

        # 2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
        if d == 0:
            nx = r - 1
            ny = c
        elif d == 1:
            nx = r
            ny = c + 1
        elif d == 2:
            nx = r + 1
            ny = c
        else:
            nx = r
            ny = c - 1
        if (0 <= nx < N) and (0 <= ny < M) and (graph[nx][ny] == 0):
            r = nx
            c = ny

    # 청소되지 않은 칸이 없는 경우
    else:
        # 1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진
        if d == 0:
            nx = r + 1
            ny = c
        elif d == 1:
            nx = r
            ny = c - 1
        elif d == 2:
            nx = r - 1
            ny = c
        else:
            nx = r
            ny = c + 1
        if (0 <= nx < N) and (0 <= ny < M) and (graph[nx][ny] != 1):
            r = nx
            c = ny
        else:
            break

print(count)
