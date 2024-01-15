import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
arrs = permutations(lst, M)
arrs = sorted(arrs)
for arr in arrs:
    print(*arr)