import sys

N, K = map(int, sys.stdin.readline().split())

lst = [i for i in range(N+1)]
visited = [0 for _ in range(N+1)]
i = 0
result = []

for _ in range(N):
    count = 0
    while count < K:
        i += 1
        if i > N:
            i = i-N
        if visited[i] == 0:
            count += 1
    visited[i] = 1
    result.append(lst[i])

print("<", str(result)[1:-1], ">", sep="")
