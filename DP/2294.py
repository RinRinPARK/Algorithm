import sys

# 사용한 동전의 최소 개수

n, k = map(int, sys.stdin.readline().split())
coins = list(set([int(sys.stdin.readline()) for _ in range(n)]))
dp = list([float('inf') for _ in range(k+1)])
dp[0] = 0

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])