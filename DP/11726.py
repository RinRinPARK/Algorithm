import sys

n = int(sys.stdin.readline())
tile = [0]*(n+1)

for i in range(n+1):
    if i < 3:
        tile[i] = i
    else:
        tile[i] = tile[i-2]+tile[i-1]

print(tile[n] % 10007)
