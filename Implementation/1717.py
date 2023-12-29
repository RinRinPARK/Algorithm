# union find 알고리즘 이용
import sys
sys.setrecursionlimit(100000)

def find(x):
    """
    이 코드는 시간초과가 남.
    if parent[x] == x:
        return x
    return find(parent[x])
    """

    # 경로압축방법으로 시간 복잡도를 줄임.
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    p, a, b = map(int, sys.stdin.readline().split())

    if p == 0:
        union(a,b)

    else:
        x = find(a)
        y = find(b)
        if (x != y):
            print("NO")
        else:
            print("YES")