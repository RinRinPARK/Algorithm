import sys
import heapq

# 최대 몇 번 동전을 움직일 수 있는지
# 만약 형택이가 동전을 무한번 움직일 수 있다면 -1을 출력
# 만약 동전이 구멍에 빠지거나, 보드의 바깥으로 나간다면 게임은 종료
dx = [-1,1,0,0]
dy = [0,0,-1,1]

H, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(H):
    board.append(list(sys.stdin.readline().strip()))

queue = []
heapq.heappush(queue, [-1,0,0])
visited = [[0 for _ in range(M)] for _ in range(H)]
answer = 0

while queue:
    v, x, y = heapq.heappop(queue)

    if (-v) >= (H * M + 1):
        answer = -1
        break

    for k in range(4):
        nx = x + (dx[k] * int(board[x][y]))
        ny = y + (dy[k] * int(board[x][y]))
        
        if (0 <= nx < H) and (0 <= ny < M) and (board[nx][ny].isdigit()) and (-visited[nx][ny] < (-v+1)):
            heapq.heappush(queue, [v - 1, nx, ny])
            visited[nx][ny] = v - 1
        else:
            answer = max(answer, -v)
print(answer)
