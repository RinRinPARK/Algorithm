import sys


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif lst[a][b][c]:
        return lst[a][b][c]
    elif a < b < c:
        lst[a][b][c] = w(a, b, c-1)+w(a, b-1, c-1)-w(a, b-1, c)
        return lst[a][b][c]
    else:
        lst[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + \
            w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return lst[a][b][c]


lst = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
while 1:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1:
        break
    else:
        val = w(a, b, c)
        print("w({}, {}, {}) = {}".format(a, b, c, val))
