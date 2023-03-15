import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.insert(0, 0)
lst = []
sums = [0 for _ in range(N+1)]
for _ in range(M):
    lst.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N+1):
    sums[i] = sums[i-1]+nums[i]

for element in lst:
    x = element[0]
    y = element[1]
    print(sums[y]-sums[x-1])
