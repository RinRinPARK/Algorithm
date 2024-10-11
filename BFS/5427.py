import sys
from collections import deque
# 벽을 통과할 수 없고, 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없다
# 얼마나 빨리 빌딩을 탈출할 수 있는지 구하는 프로그램을 작성

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(sys.stdin.readline())
for _ in range(T):
    w, h = map(int, sys.stdin.readline().split())
    graph = []

    sangeun = []
    queue = deque()
    visited = [[0 for _ in range(w)] for _ in range(h)]
    s_visited = [[0 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        lst = list(sys.stdin.readline().strip())
        for j in range(w):
            if lst[j] == '@':
                sangeun = [0, i, j]
                s_visited[i][j] = 1
                lst[j] = '.'
            elif lst[j] == '*':
                queue.append([-1, i, j])
                visited[i][j] = 1
        graph.append(lst)

    queue.append(sangeun)

    # 불 먼저 이동하고, 상근 이동
    flag = 0
    while queue:
        v, x, y = queue.popleft()

        if v == -1:
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                
                if (0 <= nx < h) and (0 <= ny < w) and (visited[nx][ny] == 0) and (graph[nx][ny] == '.'):
                    graph[nx][ny] = '*'
                    queue.append([-1, nx, ny])
                    visited[nx][ny] = 1

        else:
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if not ((0 <= nx < h) and (0 <= ny < w)):
                    print(v + 1)
                    flag = 1
                    break
                else:
                    if (s_visited[nx][ny] == 0) and (graph[nx][ny] == '.'):
                        queue.append([v + 1, nx, ny])
                        s_visited[nx][ny] = 1

            if flag == 1:
                break

    if flag != 1:
        print("IMPOSSIBLE")