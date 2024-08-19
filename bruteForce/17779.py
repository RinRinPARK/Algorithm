import sys

# 구역을 다섯 개의 선거구로 나눠야 하고, 각 구역은 다섯 선거구 중 하나에 포함
# 선거구는 구역을 적어도 하나 포함해야 하고, 한 선거구에 포함되어 있는 구역은 모두 연결
N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = float("inf")

# 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값
def calc(x, y, d1, d2):
    global result
    visited = [[0 for _ in range(N)] for _ in range(N)]

    a = []
    b = []
    c = []
    d = []
    e = []

    # 경계선 그리기
    for i in range(d1+1):
        if visited[x+i][y-i] == 0:
            visited[x+i][y-i] = 5
            e.append(lst[x+i][y-i])
    for i in range(d2+1):
        if visited[x+i][y+i] == 0:
            visited[x+i][y+i] = 5
            e.append(lst[x+i][y+i])
    for i in range(d2+1):
        if visited[x+d1+i][y-d1+i] == 0:
            visited[x+d1+i][y-d1+i] = 5
            e.append(lst[x+d1+i][y-d1+i])
    for i in range(d1+1):
        if visited[x+d2+i][y+d2-i] == 0:
            visited[x+d2+i][y+d2-i] = 5
            e.append(lst[x+d2+i][y+d2-i])

    for r1 in range(x+d1):
        for c1 in range(y+1):
            if visited[r1][c1] == 0:
                visited[r1][c1] = 1
                a.append(lst[r1][c1])
            else:
                break

    for r2 in range(x+d2, -1, -1):
        for c2 in range(N-1, y, -1):
            if visited[r2][c2] == 0:
                visited[r2][c2] = 2
                b.append(lst[r2][c2])
            else:
                break

    for r3 in range(x+d1, N):
        for c3 in range(y-d1+d2):
            if visited[r3][c3] == 0:
                visited[r3][c3] = 3
                c.append(lst[r3][c3])
            else:
                break

    for r4 in range(N-1, x+d2, -1):
        for c4 in range(N-1, y-d1+d2-1, -1):
            if visited[r4][c4] == 0:
                visited[r4][c4] = 4
                d.append(lst[r4][c4])
            else:
                break

    for v1 in range(N):
        for v2 in range(N):
            if visited[v1][v2] == 0:
                e.append(lst[v1][v2])
    
    sums = [sum(a), sum(b), sum(c), sum(d), sum(e)]

    result = min(result, max(sums) - min(sums))


for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if (x+d1+d2 <= N-1) and (0 <= y-d1 < y < y+d2 <= N-1):
                    calc(x,y,d1,d2)

print(result)