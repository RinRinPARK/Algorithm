# 연쇄행렬곱셈 알고리즘!
import sys

N = int(sys.stdin.readline())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
dp = [[float("inf") for _ in range(N)] for _ in range(N)]

for diag in range(N):
    for i in range(N-diag):
        j = i+diag
        if i == j:
            dp[i][j] = 0
        else:
            for p in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][p]+dp[p+1][j]+matrix[i][0]*matrix[p][1]*matrix[j][1])

print(dp[0][N-1])