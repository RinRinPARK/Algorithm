import sys
from itertools import permutations

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
result = 0
candidates = permutations(nums, N)

for arr in candidates:
    val = 0
    for i in range(len(arr)-1):
        val += abs(arr[i]-arr[i+1])

    result = max(result, val)

print(result)