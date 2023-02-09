import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if lst[i][j] == 1:
            houses.append([i, j])
        elif lst[i][j] == 2:
            chickens.append([i, j])

shortest = float("inf")

for combi in combinations(chickens, M):
    length = 0
    for i in range(len(houses)):
        dist = float("inf")
        for j in range(M):
            distance = abs(houses[i][0]-combi[j][0]) + \
                abs(houses[i][1]-combi[j][1])
            if distance < dist:
                dist = distance
        length += dist
    if length < shortest:
        shortest = length

print(shortest)
