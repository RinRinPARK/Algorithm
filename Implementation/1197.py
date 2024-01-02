import sys

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    x = find(a)
    y = find(b)

    if (x > y):
        parent[x] = y
    else:
        parent[y] = x

V, E = map(int,sys.stdin.readline().split())
parent = [i for i in range(V+1)]
tree = []
result = 0

for _ in range(E):
    A, B, C = map(int,sys.stdin.readline().split())
    tree.append([C, A, B])
tree.sort()

for C,A,B in tree:
    if find(A) != find(B):
        union(A, B)
        result += C

print(result)