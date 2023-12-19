import sys
import copy
from collections import deque

H, W = map(int,sys.stdin.readline().split())
graph = []
lands = []
for i in range(H):
    lst = list(sys.stdin.readline().strip())
    graph.append(lst)
    for j in range(W):
        if lst[j] == 'L':
            lands.append([i,j])

dx = [-1,1,0,0]
dy = [0,0,-1,1]
max_val = 0

for a,b in lands:
    dup = copy.deepcopy(graph)
    queue = deque()
    queue.append([a,b])
    dup[a][b] = 0
    while queue:
        x, y = queue.popleft()  
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if (0<= nx < H) and (0<=ny <W) and (dup[nx][ny] == 'L'):
                queue.append([nx,ny])
                dup[nx][ny] = dup[x][y] + 1
                if (dup[nx][ny] > max_val):
                    max_val = dup[nx][ny]


print(max_val)
