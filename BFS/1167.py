import sys
from collections import deque

V = int(sys.stdin.readline())
datas = [[] for _ in range(V+1)]

# 입력된 데이터는 모두 하나의 트리로 이어져있음
for _ in range(V):
    ipt = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(ipt)-1, 2):
        datas[ipt[0]].append([ipt[j], ipt[j+1]])

# 이어져 있는 간선들을 따라가면서 가장 큰 length를 구함
def bfs(start):
    queue = deque()
    visited = [0] * (V + 1)
    max_distance = 0
    result_vertex = 0

    queue.append((start, 0))
    visited[start] = 1

    while queue:
        current, distance = queue.popleft()

        for data in datas[current]:
            if visited[data[0]] == 0:
                visited[data[0]] = 1
                next_distance = distance + data[1]

                if next_distance > max_distance:
                    max_distance = next_distance
                    result_vertex = data[0] 

                queue.append((data[0], next_distance))

    return result_vertex, max_distance

result_vertex, result = bfs(1)
result_vertex, result = bfs(result_vertex)
print(result)