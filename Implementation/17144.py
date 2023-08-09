import sys
from collections import deque

# 확산


def spread():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    tmp_arr = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if A[i][j] != 0 and A[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < R and 0 <= ny < C and A[nx][ny] != -1:
                        tmp_arr[nx][ny] += A[i][j] // 5
                        tmp += A[i][j] // 5
                A[i][j] -= tmp

    for i in range(R):
        for j in range(C):
            A[i][j] += tmp_arr[i][j]


def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        A[x][y], before = before, A[x][y]
        x = nx
        y = ny


def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        A[x][y], before = before, A[x][y]
        x = nx
        y = ny


R, C, T = map(int, sys.stdin.readline().split())
queue = deque()
A = []
for i in range(R):
    lst = list(map(int, sys.stdin. readline().split()))
    A.append(lst)
    for j in range(C):
        if lst[j] > 0:
            queue.append([i, j])
up = -1
down = -1

for i in range(R):
    if A[i][0] == -1:
        up = i
        down = i + 1
        break

for _ in range(T):
    spread()
    air_up()
    air_down()

ans = 0
for arr in A:
    ans += sum(arr)

print(ans+2)
