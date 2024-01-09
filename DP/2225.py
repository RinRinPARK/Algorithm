"""
# 시간초과 난 dfs 코드

import sys
sys.setrecursionlimit(10**6)

N, K = map(int,sys.stdin.readline().split())
result = 0

def dfs(val, n):
    global result

    if n == K:
        if val == N:
            result += 1
        
        return
    
    for i in range(N+1):
        dfs(val+i, n+1)

dfs(0,0)
print(result%1000000000)

"""

import sys

N, K = map(int,sys.stdin.readline().split())
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
dp[0][0] = 1

for i in range(N+1):
    for j in range(1, K+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]


print(dp[N][K] % 1000000000)