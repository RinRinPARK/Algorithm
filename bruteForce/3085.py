import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0

def check():
    global answer

    # 가로 확인
    row = []
    for i in range(N):
        now = candy[i][0]
        cnt = 1
        for j in range(1, N):
            if now == candy[i][j]:
                cnt += 1
            else:
                row.append(cnt)
                cnt = 1
                now = candy[i][j]
        row.append(cnt)
    answer = max(answer, max(row))

    # 세로 확인
    column = []
    for i in range(N):
        now = candy[0][i]
        cnt = 1
        for j in range(1, N):
            if now == candy[j][i]:
                cnt += 1
            else:
                column.append(cnt)
                cnt = 1
                now = candy[j][i]
        column.append(cnt)
    answer = max(answer, max(column))


N = int(sys.stdin.readline())
candy = []
for _ in range(N):
    candy.append(list(sys.stdin.readline().strip()))

for x in range(N):
    for y in range(N):
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if (0 <= nx < N) and (0 <= ny < N):

                if candy[nx][ny] != candy[x][y]:
                    tmp = candy[x][y]
                    candy[x][y] = candy[nx][ny]
                    candy[nx][ny] = tmp

                    check()

                    tmp = candy[x][y]
                    candy[x][y] = candy[nx][ny]
                    candy[nx][ny] = tmp

print(answer)