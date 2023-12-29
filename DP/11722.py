"""
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.reverse()
dp = [0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if (A[i] > A[j]) and (dp[i] < dp[j]):
            dp[i] = dp[j]

    dp[i] += 1

print(max(dp))
"""

# 위 아래 둘 다 정답!
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if (A[i] < A[j]) and (dp[i] < dp[j]):
            dp[i] = dp[j]

    dp[i] += 1

print(max(dp))