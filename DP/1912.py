import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
result = [lst[0]]

for i in range(1, n):
    result.append(max(lst[i], result[i-1]+lst[i]))

print(max(result))
