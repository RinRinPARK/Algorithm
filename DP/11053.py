import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

result = [0]*N

for i in range(N):
    for j in range(i):
        if a[i] > a[j] and result[i] < result[j]:
            result[i] = result[j]
    result[i] += 1

print(max(result))
