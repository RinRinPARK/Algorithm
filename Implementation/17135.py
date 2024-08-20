# 미해결 - 왜틀렸는지 모르겠으요
import sys
import copy
from collections import deque

# 궁수를 배치할 수 있는 모든 경우의 수에서 최소값을 찾음
# (r1, c1), (r2, c2)의 거리는 |r1-r2| + |c1-c2|
N, M, D = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = -float("inf")

dx = [-1,-1,-1]
dy = [-1,0,1]


def attack(loc):
    global ans

    row = N
    kill = 0
    loc.sort()
    cgraph = copy.deepcopy(graph)
    killed = [[0] * M for _ in range(N)]
    lst = []
    
    # 궁사 입장에서 죽일 수 있는 적 중에 가장 가까운 적을 죽임
    while row > 0:
        shooter = [[row, loc[0]], [row, loc[1]], [row, loc[2]]]

        for a, b in shooter:
            queue = deque()
            queue.append([a-1,b,1])

            while queue:
                x, y, dist = queue.popleft()

                if cgraph[x][y] == 1:
                    lst.append([x,y])
                    if killed[x][y] == 0:
                        killed[x][y] = 1
                        kill += 1
                    break

                else:
                    for q in range(3):
                        nx = x + dx[q]
                        ny = y + dy[q]
                        if (0<=nx<N) and (0<=ny<M) and (dist+1 <= D):
                            queue.append([nx, ny, dist+1])

        row -= 1
        for u,v in lst:
            cgraph[u][v] = 0

    ans = max(ans, kill)

def dfs(d, loc):
    if d == 3:
        attack(loc)
        return

    start = loc[-1] + 1 if loc else 0  # loc가 비어있으면 0부터 시작
    for p in range(start, M):
        loc.append(p)
        dfs(d + 1, loc)
        loc.pop()

dfs(0, [])

print(ans)