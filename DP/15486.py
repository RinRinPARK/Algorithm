import sys

N = int(sys.stdin.readline().strip())
lst = [0 for _ in range(N)]
dp = [0 for _ in range(N)]

for i in range(N):
    day, cost = map(int, sys.stdin.readline().split())
    lst[i] = [day, cost]

if ( 0 <= lst[0][0]-1 < N):
    dp[lst[0][0]-1] = lst[0][1]
for k in range(1, N):
    pos = k + lst[k][0] - 1
    dp[k] = max(dp[k-1], dp[k])

    if (0 <= pos < N):
        dp[pos] = max(dp[k-1]+lst[k][1], dp[pos])

print(max(dp))