import sys
from collections import deque

# 1번 칸에서 시작해서 100번 칸에 도착하는 것
# 100번 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값
N, M = map(int, sys.stdin.readline().split())
answer = float("inf")

ladder = {}
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    ladder[a] = b

snake = {}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    snake[a] = b

queue = deque()
queue.append([1, 0])
visited = [float("inf") for _ in range(101)]
visited[1] = 0
while queue:
    x, cnt = queue.popleft()

    if x == 100:
        answer = min(answer, cnt)
        continue

    for k in range(1, 7):
        n = x + k
        if (1 <= x + k < 101):
            if (N in ladder.keys()):
                n = ladder[n]
            elif (x + k in snake.keys()):
                n = snake[n]
            
            if (visited[n] > cnt + 1):
                queue.append([n, cnt + 1])
                visited[n] = cnt + 1

print(answer)