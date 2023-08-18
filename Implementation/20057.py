import sys
import math


def action(curr, rate, ans):
    move_sand = 0
    if (A[curr[0]][curr[1]] > 0):
        for x, y, z in rate:

            nx = curr[0] + x
            ny = curr[1] + y

            if (0 <= nx < N) and (0 <= ny < N):
                if z == 0.6:
                    A[nx][ny] += (A[curr[0]][curr[1]] - move_sand)
                else:
                    sand = math.trunc(A[curr[0]][curr[1]]*z)
                    move_sand += sand
                    A[nx][ny] += sand

            else:
                if z == 0.6:
                    ans += (A[curr[0]][curr[1]] - move_sand)
                else:
                    sand = math.trunc(A[curr[0]][curr[1]]*z)
                    move_sand += sand
                    ans += sand

    A[curr[0]][curr[1]] = 0
    return ans


N = int(sys.stdin.readline())
A = []
curr = [N//2, N//2]
ans = 0

rate_2 = [(-1, +1, 0.01), (+1, +1, 0.01), (-1, 0, 0.07), (+1, 0, 0.07), (-1, -1, 0.1),
          (+1, -1, 0.1), (-2, 0, 0.02), (+2, 0, 0.02), (0, -2, 0.05), (0, -1, 0.6)]
rate_4 = [[x, -y, z] for x, y, z in rate_2]
rate_1 = [[y, x, z] for x, y, z in rate_2]
rate_3 = [[-y, x, z] for x, y, z in rate_2]

for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

for i in range(N//2):
    moves = [2]
    for _ in range(2*i+1):
        moves.append(3)
    for _ in range(2*(i+1)):
        moves.append(4)
    for _ in range(2*(i+1)):
        moves.append(1)
    for _ in range(2*(i+1)):
        moves.append(2)

    for move in moves:
        if move == 1:
            curr = [curr[0]-1, curr[1]]
            ans = action(curr, rate_1, ans)
        elif move == 2:
            curr = [curr[0], curr[1]-1]
            ans = action(curr, rate_2, ans)
        elif move == 3:
            curr = [curr[0]+1, curr[1]]
            ans = action(curr, rate_3, ans)
        else:
            curr = [curr[0], curr[1]+1]
            ans = action(curr, rate_4, ans)

print(ans)
