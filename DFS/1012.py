import sys
sys.setrecursionlimit(10**6)

x = [1, -1, 0, 0]
y = [0, 0, 1, -1]


def search(a, b):
    if a >= 0 and b >= 0 and a < M and b < N:
        if location[a][b] == 1:
            location[a][b] = 0
            for k in range(4):
                search(a+x[k], b+y[k])


for _ in range(int(sys.stdin.readline())):
    count = 0
    M, N, K = map(int, sys.stdin.readline().split())
    location = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        location[a][b] = 1

    for i in range(M):
        for j in range(N):
            if location[i][j] == 1:
                search(i, j)
                count += 1

    print(count)
