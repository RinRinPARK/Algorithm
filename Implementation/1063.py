import sys

dict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H': 8}
dict2 = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8: 'H'}
direct = {'R': [0, 1], 'L': [0, -1], 'B': [1, 0], 'T': [-1,0], 'RT': [-1, 1],
          'LT': [-1, -1], 'RB': [1, 1], 'LB': [1, -1]}

king, stone, N = map(str, sys.stdin.readline().split())
graph = [[0 for _ in range(9)] for _ in range(9)]
x, y = 9-int(king[1]), dict[king[0]]
sx, sy = 9-int(stone[1]), dict[stone[0]]
graph[x][y] = 1
graph[sx][sy] = 1

for _ in range(int(N)):
    opr = sys.stdin.readline().strip()

    dx, dy = direct[opr]
    nx = x + dx
    ny = y + dy

    if (1 <= nx < 9) and (1 <= ny < 9):

        if (nx, ny) == (sx, sy):
            if (1 <= sx + dx < 9) and (1 <= sy + dy < 9):
                graph[sx][sy] = 0
                sx = sx + dx
                sy = sy + dy
                graph[sx][sy] = 1
            else:
                continue

        graph[x][y] = 0
        x, y = nx, ny
        graph[nx][ny] = 1

print(dict2[y],9-x, sep='')
print(dict2[sy],9-sx, sep='')