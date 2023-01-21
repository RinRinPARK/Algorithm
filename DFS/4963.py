import sys
sys.setrecursionlimit(10**6)

w = 1
h = 1
x = [1, -1, 0, 0, 1, -1, -1, 1]
y = [0, 0, 1, -1, 1, 1, -1, -1]


def island(a, b, w, h):
    if lst[a][b] == 1:
        lst[a][b] = 0
        for i in range(8):
            if a+x[i] >= 0 and b+y[i] >= 0 and a+x[i] < h and b+y[i] < w:
                island(a+x[i], b+y[i], w, h)


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    lst = []
    count = 0
    for _ in range(h):
        lst.append(list(map(int, sys.stdin.readline().split())))
    for i in range(h):
        for j in range(w):
            if lst[i][j] == 1:
                island(i, j, w, h)
                count += 1
    print(count)
