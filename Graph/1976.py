import sys

# 도시들의 개수와 도시들 간의 연결 여부가 주어져 있고, 
# 동혁이의 여행 계획에 속한 도시들이 순서대로 주어졌을 때 가능한지 여부를 판별
# 같은 도시를 여러 번 방문하는 것도 가능

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parents = [k for k in range(N+1)]

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parents[a] = b
    else:
        parents[b] = a

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

for i in range(1, N + 1):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if lst[j] == 1:
            union(i, j+1)

plan = list(map(int, sys.stdin.readline().split()))

for k in range(len(plan)-1):

    if find(plan[k]) != find(plan[k+1]):
        print("NO")
        exit()

print("YES")