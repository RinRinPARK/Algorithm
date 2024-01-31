import sys
from collections import deque

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

blue = 0
white = 0
queue = deque()
queue.append([0,0,N,N])

while queue:
    lx,ly,rx,ry = queue.popleft()
    clr = graph[lx][ly]
    check = 0

    for i in range(lx, rx):
        for j in range(ly, ry):
            if graph[i][j] != clr:
                check = 1
                queue.append([lx,ly,(lx+rx)//2,(ly+ry)//2])
                queue.append([(lx+rx)//2,ly,rx,(ly+ry)//2])
                queue.append([lx,(ly+ry)//2,(lx+rx)//2,ry])
                queue.append([(lx+rx)//2,(ly+ry)//2,rx,ry])
                break
        if check == 1:
            break
    
    if (check == 0):
        if clr == 1:
            blue += 1
        else:
            white += 1

print(white)
print(blue)

