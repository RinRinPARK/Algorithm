import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
queue = deque()
dist = [0]*100001
queue.append(N)


def bfs():
    while queue:
        a = queue.popleft()
        if a == K:
            print(dist[a])
            break
        for nx in (a-1, a+1, a*2):
            if nx >= 0 and nx <= 100000 and dist[nx] == 0:
                queue.append(nx)
                dist[nx] = dist[a]+1


bfs()
