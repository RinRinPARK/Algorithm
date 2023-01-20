import sys
sys.setrecursionlimit(10**6)


def found(n):
    visit[n] = 1
    for m in lst[n]:
        if not visit[m]:
            found(m)


N, M = map(int, sys.stdin.readline().split())
lst = [[] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
count = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    lst[a].append(b)
    lst[b].append(a)

for i in range(1, N+1):
    if not visit[i]:
        found(i)
        count += 1

print(count)
