import sys

"""
시간 초과가 났던 move함수

def move(x, y, graph, temp):
    s, d, z = graph[x][y]
    graph[x][y] = 0
    for _ in range(s):
        if d == 1:
            if (0 <= x - 1):
                x -= 1
            elif (x-1 < 0):
                x += 1
                d = 2
        elif d == 2:
            if (x+1 < R):
                x += 1
            elif (x+1 >= R):
                x -= 1
                d = 1
        elif d == 3:
            if (y+1 < C):
                y += 1
            elif (y+1 >= C):
                y -= 1
                d = 4
        else:
            if (y-1 >= 0):
                y -= 1
            elif (y-1 < 0):
                y += 1
                d = 3
"""


def move(x, y, graph, temp):
    s, d, z = graph[x][y]
    ns = s
    graph[x][y] = 0

    # 시간 절약을 위해 한 번에 갈 수 있는 만큼 움직이기
    while s > 0:
        if d == 1:
            if (x - s) >= 0:
                x -= s
                s = 0
            else:
                s -= x
                x = 0
                d = 2

        elif d == 2:
            if (x + s) < R:
                x += s
                s = 0
            else:
                s -= (R-1-x)
                x = R-1
                d = 1

        elif d == 3:
            if (y + s) < C:
                y += s
                s = 0
            else:
                s -= (C-1-y)
                y = C-1
                d = 4
        else:
            if (y - s) >= 0:
                y -= s
                s = 0
            else:
                s -= y
                y = 0
                d = 3

    if temp[x][y] == 0:
        temp[x][y] = [ns, d, z]
        sharks.append([x, y])
    else:
        # 상어 잡아먹기
        if z > temp[x][y][2]:
            temp[x][y] = [ns, d, z]


R, C, M = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(C)] for _ in range(R)]
ans = 0
sharks = []

for _ in range(M):
    # r, c, s, d, z // (r, c)위치, s속력, d이동 방향, z크기
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    graph[r-1][c-1] = [s, d, z]
    sharks.append([r-1, c-1])

for h in range(C):

    # 상어 낚시
    for i in range(R):
        if graph[i][h] != 0:
            ans += graph[i][h][2]
            graph[i][h] = 0
            sharks.remove([i, h])
            break

    # 상어 이동, 잡아먹기
    temp = [[0 for _ in range(C)] for _ in range(R)]
    for _ in range(len(sharks)):
        x, y = sharks.pop(0)
        move(x, y, graph, temp)
    graph = temp

print(ans)
