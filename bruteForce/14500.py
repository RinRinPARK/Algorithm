
"""
힙큐를 이용해 부르트포스로 풀었는데 자꾸 시간초과가 남.
다중 반복문이라 그런 것 같긴 한데,
도저히 시간복잡도를 줄일 방법이 떠오르지 않음.  ㅠㅠ
"""
"""
import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

for i in range(N):
    for j in range(M):
        heap = []
        visited = [[0 for _ in range(M)] for _ in range(N)]
        count = 0
        value = 0
        heapq.heappush(heap, [-graph[i][j], i, j])
        while count < 4:
            val, x, y = heapq.heappop(heap)
            visited[x][y] = 1
            count += 1
            value -= val
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if (0 <= nx < N) and (0 <= ny < M) and (visited[nx][ny] == 0):
                    heapq.heappush(heap, [-graph[nx][ny], nx, ny])
        result = max(result, value)

print(result)

"""
"""
논리적 오류가 있음, 애초에 이 문제는 그래프만으로는 풀 수 없는 문제임 먼가 응용이 필요함
-> 왜냐면.. 모든 테트로미노 모양을 만들 수 없기 때문

import sys

N, M = map(int, sys.stdin.readline().split())
graph = []

for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 0

# x좌표, y좌표, 칸 개수, 칸에 쓰여있는 수의 합
def dfs(x, y, count, value):
    global result

    if count == 4:
        result = max(result, value)
    
    else:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if (0<= nx < N) and (0<= ny < M) and (graph[nx][ny] != -1):
                imsi = graph[nx][ny]
                graph[nx][ny] = -1
                dfs(nx,ny,count + 1, value + imsi)
                graph[nx][ny] = imsi
                



for i in range(N):
    for j in range(M):
        val = graph[i][j]
        graph[i][j] = -1
        dfs(i,j, 1, val)
        graph[i][j] = val

print(result)
"""

# 테트로미노의 19가지 경우에 대한 좌표
tetrominoes = [
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(2, 0), (2, 1), (1, 1), (0, 1)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(1, 0), (1, 1), (1, 2), (0, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(1, 0), (0, 1), (1, 1), (2, 1)],
    [(1, 0), (2, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (0, 1), (1, 1), (0, 2)],
    [(0, 0), (0, 1), (1, 1), (1, 2)]
]

import sys

N, M = map(int, sys.stdin.readline().split())
graph = []
result = 0

for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))

def calc_sum(x,y):
    global result 

    for arr in tetrominoes:
        value = 0
        for dx, dy in arr:
            nx = x + dx
            ny = y + dy
            if (0<=nx<N) and (0<=ny<M):
                value += graph[nx][ny]
            else:
                break
        result = max(result, value)


for i in range(N):
    for j in range(M):
        calc_sum(i,j)

print(result)