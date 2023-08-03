import sys
import copy


def draw(graph, nx, ny, p):
    if p == 0:
        nx += 1
        graph[ny][nx] = 1
    elif p == 1:
        ny -= 1
        graph[ny][nx] = 1
    elif p == 2:
        nx -= 1
        graph[ny][nx] = 1
    else:
        ny += 1
        graph[ny][nx] = 1
    return nx, ny


N = int(sys.stdin.readline())
graph = [[0 for _ in range(101)] for _ in range(101)]

# 하나씩 입력 받으면서 바로 그리기
# 이전 세대의 정보를 뒤집고 각각 +1해서 붙이기
for _ in range(N):
    x, y, d, g = map(int, sys.stdin.readline().split())
    graph[y][x] = 1
    lst = [d]
    # 세대 끝까지
    for k in range(g):
        new = []
        for q in range(len(lst) - 1, -1, -1):
            new.append((lst[q]+1) % 4)
        lst.extend(new)
    nx = x
    ny = y
    for act in lst:
        nx, ny = draw(graph, nx, ny, act)

ans = 0
# 정사각형 개수 구하기
for i in range(100):
    for j in range(100):
        if (graph[i][j] == 1) and (graph[i+1][j] == 1) and (graph[i][j+1] == 1) and (graph[i+1][j+1] == 1):
            ans += 1
print(ans)
