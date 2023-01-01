import sys

N = int(sys.stdin.readline())
value = []

for _ in range(N):
    value.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    value[i][0] = min(value[i-1][1], value[i-1][2])+value[i][0]
    value[i][1] = min(value[i-1][0], value[i-1][2])+value[i][1]
    value[i][2] = min(value[i-1][1], value[i-1][0])+value[i][2]

print(min(value[N-1][0], value[N-1][1], value[N-1][2]))
