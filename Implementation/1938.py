import sys
import heapq

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]


N = int(sys.stdin.readline())
board = []
wood = [] # 중심점, 가로0/세로1
finish = []
for i in range(N):
    lst = list(sys.stdin.readline().strip())
    for j in range(N):
        if lst[j] == 'B':
            wood.append([i,j])
            lst[j] = '0'
        elif lst[j] == 'E':
            finish.append([i, j])
            lst[j] = '0'
    board.append(lst)

finish.sort()
wood.sort()
w = [0]
if wood[0][0] == wood[1][0]:
    w.append(0) # 가로
else:
    w.append(1) # 세로

# 좌표 저장
w.append(wood)

queue = []
heapq.heappush(queue, w)
answer = float("inf")
visited = [[[float("inf"),float("inf")] for _ in range(N)] for _ in range(N)]

while queue:
    v, dir, coor = heapq.heappop(queue)

    if coor == finish:
        answer = v
        break


    for k in range(4):
        flag = 0
        for x, y in coor:
            nx = x + dx[k]
            ny = y + dy[k]

            if (0 <= nx < N) and (0 <= ny < N) and (board[nx][ny] == '0'):
                continue
            else:
                flag = 1
                break

        if flag == 0:
            new = []
            for x, y in coor:
                nx = x + dx[k]
                ny = y + dy[k]
                new.append([nx, ny])
            new.sort()
            if visited[new[1][0]][new[1][1]][dir] > v + 1:
                visited[new[1][0]][new[1][1]][dir] = v + 1
                heapq.heappush(queue, [v + 1, dir, new])

    # 회전 가능한지 확인
    flag_t = 0
    for k in range(8):
        nx = coor[1][0] + dx[k]
        ny = coor[1][1] + dy[k]

        if (0 <= nx < N) and (0 <= ny < N) and (board[nx][ny] == '0'):
            continue
        else:
            flag_t = 1
            break

    if flag_t == 0:
        if (dir == 0) and (visited[coor[1][0]][coor[1][1]][1] > v + 1):
            new = [[coor[1][0] - 1, coor[1][1]], [coor[1][0], coor[1][1]], [coor[1][0] + 1, coor[1][1]]]
            heapq.heappush(queue, [v + 1, 1, new])
        elif (dir == 1) and (visited[coor[1][0]][coor[1][1]][0] > v + 1):
            new = [[coor[1][0], coor[1][1] - 1], [coor[1][0], coor[1][1]], [coor[1][0], coor[1][1] + 1]]
            heapq.heappush(queue, [v + 1, 0, new])

if answer == float("inf"):
    print(0)
else:
    print(answer)