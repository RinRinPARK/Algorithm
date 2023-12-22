import sys
from itertools import combinations

heights = []
for _ in range(9):
    heights.append(int(sys.stdin.readline()))

lsts = combinations(heights, 7)
for arr in lsts:
    if sum(arr) == 100:
        arr = sorted(arr)
        for i in range(7):
            print(arr[i])
        break