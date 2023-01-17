import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
computer = [[] for i in range(N+1)]
visit = [0]*(N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    computer[a].append(b)
    computer[b].append(a)  # 양방향


def research(n):
    visit[n] = 1
    arr = computer[n]
    for j in arr:
        if visit[j] == 0:
            research(j)


research(1)

print(sum(visit)-1)
