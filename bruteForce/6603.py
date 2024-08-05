import sys
from itertools import combinations

while True:
    lst = list(map(int, sys.stdin.readline().split()))

    if (len(lst) == 1) and (lst[0] == 0):
        break

    n = lst.pop(0)

    candidates = combinations(lst, 6)

    for i in candidates:
        print(*i)
    print()