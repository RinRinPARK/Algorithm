from collections import deque

R, C, K = map(int, input().split())
R += 3
lst = []
for _ in range(K):
    lst.append(list(map(int, input().split())))
graph = [[0 for _ in range(C)] for _ in range(R)]
answer = 0

def check(m, n):
    if (0 <= m < R) and (0 <= n < C):
        return True
    return False

for k in range(len(lst)):
    x, y, d, num = 1, lst[k][0]-1, lst[k][1], k + 1

    while True:
        # 내려 갈 수 있으면 내려가기
        if (check(x+2, y)) and (check(x+1, y-1)) and (check(x+1, y+1)) and (graph[x + 2][y] == 0) and (graph[x + 1][y - 1] == 0) and (graph[x + 1][y + 1] == 0):
            x += 1

        # 서쪽으로 회전 가능하면 회전하기
        elif (check(x-1, y-1)) and (check(x, y-2)) and (check(x+1, y-1)) and (check(x+1, y-2)) and (check(x+2, y - 1)) and (graph[x - 1][y - 1] == 0) and (graph[x][y - 2] == 0) and (graph[x + 1][y - 1] == 0) and (graph[x + 1][y - 2] == 0) and (graph[x + 2][y - 1] == 0):
            x += 1
            y -= 1
            d = (d + 3) % 4
        # 동쪽으로 회전 가능하면 회전하기
        elif (check(x-1, y+1)) and (check(x, y + 2)) and (check(x+1, y + 1)) and (check(x+1, y+2)) and (check(x+2, y+1)) and (graph[x - 1][y + 1] == 0) and (graph[x][y + 2] == 0) and (graph[x + 1][y + 1] == 0) and (graph[x + 1][y + 2] == 0) and (graph[x + 2][y + 1] == 0):
            x += 1
            y += 1
            d = (d + 1) % 4

        else:
            break
    # 더이상 이동할 수 없다면
    if (check(x-3, y)) and (check(x-3, y-1)) and (check(x-1-3, y)) and (check(x-3, y+1)) and (check(x+1-3, y)):
        # 골렘 채우기
        graph[x][y] = num
        graph[x][y - 1] = num
        graph[x - 1][y] = num
        graph[x][y + 1] = num
        graph[x + 1][y] = num
        if d == 0:
            graph[x - 1][y] = -num
        elif d == 1:
            graph[x][y + 1] = -num
        elif d == 2:
            graph[x + 1][y] = -num
        else:
            graph[x][y - 1] = -num

        # 제일 남쪽으로 정령 이동하기
        q = deque()
        q.append([x, y, num])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        max_x = 0
        visited = [[0 for _ in range(C)] for _ in range(R)]
        visited[x][y] = 1

        while q:
            a, b, n = q.popleft()
            max_x = max(max_x, a - 2)

            for p in range(4):
                na = a + dx[p]
                nb = b + dy[p]

                if (3 <= na < R) and (0 <= nb < C) and (graph[na][nb] != 0) and (visited[na][nb] == 0):
                    if abs(graph[na][nb]) == abs(n):
                        q.append([na, nb, graph[na][nb]])
                        visited[na][nb] = 1
                    elif (n < 0) and (abs(graph[na][nb]) != abs(n)):
                        q.append([na, nb, graph[na][nb]])
                        visited[na][nb] = 1
    
        answer += max_x


    # 골렘 일부가 숲을 벗어나 있다면
    else:
        # 골렘 다 빼기
        graph = [[0 for _ in range(C)] for _ in range(R)]


print(answer)