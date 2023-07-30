import sys
import copy

N, L = map(int, sys.stdin.readline().split())
graph = []
fail = 0

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


# 뒤에 오는게 낮은 경우, 높은 경우로 나눠서 생각
for i in range(N):
    breaker = 0
    cpy = [[0 for _ in range(N)] for _ in range(N)]
    for j in range(N-1):
        if graph[i][j] == graph[i][j+1]:
            continue
        elif abs(graph[i][j]-graph[i][j+1]) == 1:
            # 뒤에 오는게 낮은 경우 + L을 충족 못할 경우
            if graph[i][j] > graph[i][j+1]:
                if cpy[i][j+1] == 1:
                    fail += 1
                    breaker = 1
                    break
                cpy[i][j+1] = 1
                for k in range(1, L):
                    if (0 > (j+1+k)) or ((j+1+k) >= N) or (graph[i][j+1] != graph[i][j+1+k]) or (cpy[i][j+1+k] == 1):
                        fail += 1
                        breaker = 1
                        break
                    else:
                        cpy[i][j+1+k] = 1
            # 뒤에 오는게 높은 경우 + L을 충족 못할 경우
            else:
                if cpy[i][j] == 1:
                    fail += 1
                    breaker = 1
                    break
                cpy[i][j] = 1
                for k in range(1, L):
                    if (0 > (j-k)) or ((j-k) >= N) or (graph[i][j] != graph[i][j-k]) or (cpy[i][j-k] == 1):
                        fail += 1
                        breaker = 1
                        break
                    else:
                        cpy[i][j-k] = 1
        else:
            fail += 1
            breaker = 1

        if breaker == 1:
            break

for m in range(N):
    arr = []
    for n in range(N):
        arr.append(graph[n][m])

    breaker = 0
    cpy = [[0 for _ in range(N)] for _ in range(N)]
    for p in range(N-1):
        if arr[p] == arr[p+1]:
            continue
        elif abs(arr[p]-arr[p+1]) == 1:
            # 뒤에 오는게 낮은 경우 + L을 충족 못할 경우
            if arr[p] > arr[p+1]:
                if cpy[p+1][m] == 1:
                    fail += 1
                    breaker = 1
                    break
                cpy[p+1][m] = 1
                for k in range(1, L):
                    if (0 > (p+1+k)) or ((p+1+k) >= N) or (arr[p+1] != arr[p+1+k]) or (cpy[p+1+k][m] == 1):
                        fail += 1
                        breaker = 1
                        break
                    else:
                        cpy[p+1+k][m] = 1
            # 뒤에 오는게 높은 경우 + L을 충족 못할 경우
            else:
                if cpy[p][m] == 1:
                    fail += 1
                    breaker = 1
                    break
                cpy[p][m] = 1
                for k in range(1, L):
                    if (0 > (p-k)) or ((p-k) >= N) or (arr[p] != arr[p-k]) or (cpy[p-k][m] == 1):
                        fail += 1
                        breaker = 1
                        break
                    else:
                        cpy[p-k][m] = 1
        else:
            fail += 1
            breaker = 1

        if breaker == 1:
            break

print(int(2*N) - fail)
