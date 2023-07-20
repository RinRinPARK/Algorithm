import sys


def move(direction):
    global graph
    global dice
    global x, y
    a, b, c, d, e, f = dice[:]

    # 굴리기
    if direction == 1:  # 동
        if ((y + 1) >= 0) and ((y + 1) < M):
            y += 1
            dice = [a, e, c, f, d, b]
        else:
            return
    elif direction == 2:  # 서
        if ((y - 1) >= 0) and ((y-1) < M):
            y -= 1
            dice = [a, f, c, e, b, d]
        else:
            return
    elif direction == 3:  # 북
        if ((x-1) >= 0) and ((x-1) < N):
            x -= 1
            dice = [d, a, b, c, e, f]
        else:
            return
    else:  # 남
        if ((x+1) >= 0) and ((x+1) < N):
            x += 1
            dice = [b, c, d, a, e, f]
        else:
            return

    # 숫자 바꾸기
    if graph[x][y] == 0:
        graph[x][y] = dice[3]
        dice[3] = 0
    else:
        dice[3] = graph[x][y]
        graph[x][y] = 0

    print(dice[1])


N, M, x, y, K = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
order = list(map(int, sys.stdin.readline().split()))
dice = [0, 0, 0, 0, 0, 0]

for num in order:
    move(num)
