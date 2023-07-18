import sys
from itertools import product
import copy


def up(map, N):

    for i in range(N-1):
        for j in range(N):
            for m in range(i+1, N):
                if map[m][j] != 0:
                    if map[i][j] == map[m][j]:
                        map[i][j] += map[m][j]
                        map[m][j] = 0
                        break
                    break

    for i in range(N-1):
        for j in range(N):
            if map[i][j] == 0:
                for m in range(i+1, N):
                    if map[m][j] != 0:
                        map[i][j] = map[m][j]
                        map[m][j] = 0
                        break


def down(map, N):

    for i in range(N-1, 0, -1):
        for j in range(N):
            for m in range(i-1, -1, -1):
                if map[m][j] != 0:
                    if map[i][j] == map[m][j]:
                        map[i][j] += map[m][j]
                        map[m][j] = 0
                        break
                    break

    for i in range(N-1, 0, -1):
        for j in range(N):
            if map[i][j] == 0:
                for m in range(i-1, -1, -1):
                    if map[m][j] != 0:
                        map[i][j] = map[m][j]
                        map[m][j] = 0
                        break


def left(map, N):

    for i in range(N-1):
        for j in range(N):
            for m in range(i+1, N):
                if map[j][m] != 0:
                    if map[j][i] == map[j][m]:
                        map[j][i] += map[j][m]
                        map[j][m] = 0
                        break
                    break

    for i in range(N-1):
        for j in range(N):
            if map[j][i] == 0:
                for m in range(i+1, N):
                    if map[j][m] != 0:
                        map[j][i] = map[j][m]
                        map[j][m] = 0
                        break


def right(map, N):

    for i in range(N-1, 0, -1):
        for j in range(N):
            for m in range(i-1, -1, -1):
                if map[j][m] != 0:
                    if map[j][i] == map[j][m]:
                        map[j][i] += map[j][m]
                        map[j][m] = 0
                        break
                    break

    for i in range(N-1, 0, -1):
        for j in range(N):
            if map[j][i] == 0:
                for m in range(i-1, -1, -1):
                    if map[j][m] != 0:
                        map[j][i] = map[j][m]
                        map[j][m] = 0
                        break


N = int(sys.stdin.readline())
graph = []
actions = []
result = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 일단 permutations로 움직이는 경우의 수를 모두 수집
# 각 경우에 따라 움직여보면서 그 결과의 최댓값을 한 리스트에 저장
# 최대 결과 모음 리스트에서 또 최댓값을 찾아 return

# 움직일 수 있는 모든 경우의 수 구하기
for i in range(1, 6):
    for ele in product(["u", "d", "l", "r"], repeat=i):
        actions.append(ele)

# 움직여 보기
for lst in actions:
    map = copy.deepcopy(graph)

    # 움직이기
    for k in range(len(lst)):
        if lst[k] == 'u':
            up(map, N)
        elif lst[k] == 'd':
            down(map, N)
        elif lst[k] == 'l':
            left(map, N)
        else:
            right(map, N)

    # 최댓값 구해서 저장하기
    maximum = 0
    for j in range(N):
        maximum = max(maximum, max(map[j]))

    result.append(maximum)

print(max(result))
