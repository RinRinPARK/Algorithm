import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.insert(0, 0)
sums = [0]
result = [0 for _ in range(M)]
count = 0

for k in range(1, len(lst)):
    sums.append(sums[k-1]+lst[k])

for i in range(1, len(sums)):
    sums[i] = sums[i] % M
    if sums[i] == 0:
        count += 1
    result[sums[i]] += 1

for j in range(M):
    if result[j] > 1:
        count += (result[j]*(result[j]-1)//2)

print(count)
