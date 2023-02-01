import sys
from collections import deque

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

for _ in range(int(sys.stdin.readline())):
    lst = []
    queue = deque()
    l = int(sys.stdin.readline())
    visited = [[0]*l for _ in range(l)]
    for _ in range(2):
        lst.append(list(map(int, sys.stdin.readline().split())))
    if (lst[0][0] == lst[1][0]) and (lst[0][1] == lst[1][1]):
        print(0)
    else:
        queue.append(lst[0])
        while queue:
            a, b = queue.popleft()
            if (a == lst[1][0]) and (b == lst[1][1]):
                print(visited[a][b])
                queue.clear()
                break
            else:
                for i in range(8):
                    nx = a+dx[i]
                    ny = b+dy[i]
                    if (0 <= nx < l) and (0 <= ny < l) and (visited[nx][ny] == 0):
                        queue.append([nx, ny])
                        visited[nx][ny] = visited[a][b]+1
