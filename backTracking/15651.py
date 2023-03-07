import sys

N, M = map(int, sys.stdin.readline().split())

lst = []


def dfs():
    if len(lst) == M:
        print(*lst)
    else:
        for i in range(1, N+1):
            lst.append(i)
            dfs()
            lst.pop()


dfs()
