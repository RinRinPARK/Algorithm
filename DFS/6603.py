import sys

def dfs(n, idx, current):
    if n == 6:
        print(*current)

    for i in range(idx, len(lst)):
        current.append(lst[i])
        dfs(n+1, i+1, current)
        current.pop()



while True:
    lst = list(map(int, sys.stdin.readline().split()))

    if (len(lst) == 1) and (lst[0] == 0):
        break

    l = lst.pop(0)

    dfs(0, 0, [])
    print()