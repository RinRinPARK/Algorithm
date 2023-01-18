import sys
import copy
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
lst = []
x = [1, -1, 0, 0]
y = [0, 0, 1, -1]
result = []
startVal = 0

for _ in range(N):
    new = list(map(int, sys.stdin.readline().split()))
    lst.append(new)
    if startVal < max(new):
        startVal = max(new)


def flood(n, a, b, graph):
    if a >= 0 and b >= 0 and a < N and b < N:
        if graph[a][b] > n:
            graph[a][b] = 0
            for i in range(4):
                flood(n, a+x[i], b+y[i], graph)


for i in range(startVal):
    count = 0
    lctn = copy.deepcopy(lst)
    for a in range(N):
        for b in range(N):
            if lctn[a][b] > i:
                flood(i, a, b, lctn)
                count += 1
    result.append(count)

print(max(result))
