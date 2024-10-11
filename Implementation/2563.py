import sys

N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
graph = [[0 for _ in range(100)] for _ in range(100)]
answer = 0

for a, b in lst:
    for x in range(100-b-10, 100-b):
        for y in range(a, a + 10):

            if graph[x][y] == 0:
                graph[x][y] = 1
                answer += 1

print(answer)
