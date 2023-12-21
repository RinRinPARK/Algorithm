# BFS로 구현한 코드. 시간초과
"""
import sys
from collections import deque
import copy

R, C = map(int, sys.stdin.readline().split())
graph = []

for _ in range(R):
    graph.append(list(sys.stdin.readline().strip()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 0
queue = deque()
# [행좌표, 열좌표, 지난 칸 개수, 지나온 칸 리스트]
queue.append([0,0,1,[graph[0][0]]])

while queue:
    x, y, count, lst = queue.popleft()
    flag = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<=nx<R) and (0<=ny<C) and (graph[nx][ny] not in lst):
            flag = 1
            new_lst = copy.deepcopy(lst)
            new_lst.append(graph[nx][ny])
            queue.append([nx, ny, count +1, new_lst])

    if flag == 0:
        result = max(result, count)

print(result)

"""
import sys

# x좌표(행좌표), y좌표(열좌표), 지나온 칸 개수, 지나온 칸 문자 집합
def dfs(x, y, count):
    global result

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<=nx<R) and (0<=ny<C) and (graph[nx][ny] not in lst):
            lst.add(graph[nx][ny])
            dfs(nx, ny, count + 1)
            lst.remove(graph[nx][ny])
    
    result = max(result, count)

R, C = map(int, sys.stdin.readline().split())
graph = []

for _ in range(R):
    graph.append(list(sys.stdin.readline().strip()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 0
lst = set()
lst.add(graph[0][0])

dfs(0,0,1)  

print(result)