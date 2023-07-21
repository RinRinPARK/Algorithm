import sys

N = int(sys.stdin.readline())
lst = []
dp = [0 for _ in range(N+1)]

for _ in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(i+lst[i][0], N+1):
        if dp[j] < dp[i] + lst[i][1]:
            dp[j] = dp[i] + lst[i][1]

print(dp[-1])
