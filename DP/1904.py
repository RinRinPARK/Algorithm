"""
메모리 초과 코드

import sys

N = int(sys.stdin.readline())
dp = [0 for _ in range(N+1)]
dp[0] = 1
dp[1] = 1

for k in range(2, N+1):
    dp[k] = dp[k-2] + dp[k-1]

print(dp[N])
"""

import sys

N = int(sys.stdin.readline())
dp = [0 for _ in range(N+1)]
dp[0] = 1
dp[1] = 1

for k in range(2, N+1):
    dp[k] = (dp[k-2] + dp[k-1])%15746

print(dp[N])