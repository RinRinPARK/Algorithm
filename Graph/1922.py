# 모든 컴퓨터를 연결하는데 필요한 최소비용을 출력
# mst - kruskal알고리즘
# 가중치에 따라 오름차순으로 정렬하고 하나씩 연결해보며 cycle이 발생하면 다음 경로로
import sys

N = int(sys.stdin.readline())
parent = [i for i in range(N+1)]
M = int(sys.stdin.readline())
graph = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append([c, a, b])
graph.sort()

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(x, y):
    fx = find(x)
    fy = find(y)
    if fx < fy:
        parent[fy] = fx
    else:
        parent[fx] = fy


result = 0
for c, a, b in graph:
    if find(a) == find(b):
        continue
    union(a,b)
    result += c

print(result)