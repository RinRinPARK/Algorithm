import sys


def R(graph):
    max_len = 0
    for i in range(len(graph)):
        dict = {}
        arr = []
        for j in graph[i]:
            if j == 0:
                continue
            if j in dict:
                dict[j] += 1
            else:
                dict[j] = 1
        graph[i] = []
        for k in dict.keys():
            arr.append([k, dict[k]])
        arr.sort(key=lambda x: (x[1], x[0]))
        for p in range(len(arr)):
            graph[i].append(arr[p][0])
            graph[i].append(arr[p][1])
        max_len = max(max_len, len(graph[i]))

    for m in range(len(graph)):
        while max_len > len(graph[m]):
            graph[m].append(0)


r, c, k = map(int, sys.stdin.readline().split())
count = 0
r, c = r-1, c-1
A = []
for _ in range(3):
    A.append(list(map(int, sys.stdin.readline().split())))

for _ in range(101):

    row = len(A)
    column = len(A[0])

    if (0 <= r < row) and (0 <= c < column) and A[r][c] == k:
        break

    count += 1
    if row >= column:
        R(A)
    else:
        # A 행렬 transpose
        A = list(map(list, zip(*A)))
        R(A)
        A = list(map(list, zip(*A)))

if count > 100:
    print(-1)
else:
    print(count)
