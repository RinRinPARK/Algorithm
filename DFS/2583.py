import sys
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
M, N, K = map(int, sys.stdin.readline().split())
lst = [[0 for _ in range(M)] for _ in range(N)]


def coloring(x, y, lx, ly, rx, ry):
    for i in range(lx, rx):
        for j in range(ly, ry):
            lst[i][j] = 1

    # lst[x][y] = 1
    # for i in range(4):
    #     nx = x+dx[i]
    #     ny = y+dy[i]
    #     if lx <= nx < rx and ly <= ny < ry:
    #         if lst[nx][ny] == 0:
    #             coloring(nx, ny, lx, ly, rx, ry)


for _ in range(K):
    lx, ly, rx, ry = map(int, sys.stdin.readline().split())
    coloring(lx, ly, lx, ly, rx, ry)


def count(x, y):
    global num
    num += 1
    lst[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if lst[nx][ny] == 0:
                count(nx, ny)


result = []
for i in range(N):
    for j in range(M):
        num = 0
        if lst[i][j] == 0:
            count(i, j)
            result.append(num)

print(len(result))
result.sort()
print(*result)
