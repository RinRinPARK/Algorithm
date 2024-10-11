import sys

# 서로 다른 세 씨앗을 모두 꽃이 피게하면서 가장 싼 가격에 화단을 대여
# 꽃잎이 핀 모양을 기준으로 대여를 해야하므로 꽃 하나당 5평의 땅을 대여
dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(sys.stdin.readline())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = float("inf")

def dfs(num, c):
    global answer

    if num == 3:
        answer = min(answer, c)
        return 

    for x in range(N):
        for y in range(N):

            flag = 0

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if (0 <= nx < N) and (0 <= ny < N) and (visited[nx][ny] == 0):
                    continue
                else:
                    flag = 1

            if flag == 0:
                whole_c = costs[x][y]
                visited[x][y] = 1

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    visited[nx][ny] = 1
                    whole_c += costs[nx][ny]

                dfs(num + 1, c + whole_c)

                visited[x][y] = 0

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    visited[nx][ny] = 0

                

    return

visited = [[0 for _ in range(N)] for _ in range(N)]
dfs(0, 0)

print(answer)