import sys

N = int(sys.stdin.readline())
dp = [[1] for _ in range(1001)]
dp[1] = [1,1,1,1,1,1,1,1,1,1]
dp[2] = [1,2,3,4,5,6,7,8,9,10]

for i in range(3, N+1):
    for j in range(1, 10):
        dp[i].append(dp[i][j-1]+dp[i-1][j])

print(sum(dp[N])%10007)