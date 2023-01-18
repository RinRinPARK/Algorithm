import sys
import copy
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
graph = []
x = [1, -1, 0, 0]
y = [0, 0, 1, -1]
nrml_count = 0
blnd_count = 0

for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

blind_graph = copy.deepcopy(graph)
normal_graph = copy.deepcopy(graph)


def RG(g, a, b):
    if a >= 0 and b >= 0 and a < N and b < N:
        if g[a][b] == "R" or g[a][b] == "G":
            g[a][b] = "V"
            for i in range(4):
                RG(g, a+x[i], b+y[i])


def R(g, a, b):
    if a >= 0 and b >= 0 and a < N and b < N:
        if g[a][b] == "R":
            g[a][b] = "V"
            for i in range(4):
                R(g, a+x[i], b+y[i])


def G(g, a, b):
    if a >= 0 and b >= 0 and a < N and b < N:
        if g[a][b] == "G":
            g[a][b] = "V"
            for i in range(4):
                G(g, a+x[i], b+y[i])


def B(g, a, b):
    if a >= 0 and b >= 0 and a < N and b < N:
        if g[a][b] == "B":
            g[a][b] = "V"
            for i in range(4):
                B(g, a+x[i], b+y[i])


for i in range(N):
    for j in range(N):
        if blind_graph[i][j] != "V":
            if blind_graph[i][j] == "R" or blind_graph[i][j] == "G":
                RG(blind_graph, i, j)
                blnd_count += 1
            elif blind_graph[i][j] == "B":
                B(blind_graph, i, j)
                blnd_count += 1

for i in range(N):
    for j in range(N):
        if normal_graph[i][j] != "V":
            if normal_graph[i][j] == "R":
                R(normal_graph, i, j)
                nrml_count += 1
            elif normal_graph[i][j] == "G":
                G(normal_graph, i, j)
                nrml_count += 1
            elif normal_graph[i][j] == "B":
                B(normal_graph, i, j)
                nrml_count += 1

print(blnd_count)
print(nrml_count)
