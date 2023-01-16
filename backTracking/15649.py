import sys

N, M = map(int, sys.stdin.readline().split())

lst = []


def sequence():
    if len(lst) == M:
        print(' '.join(map(str, lst)))

    for i in range(1, N+1):
        if i not in lst:
            lst.append(i)
            sequence()
            lst.pop()


sequence()
