# 식 세우면서 점화식을 찾긴 했는데
# 숫자들에서 규칙을 찾은거라 어떠한 원리로 dp[i-1]*2+dp[i-2]인지는 풀이법을 봐도 잘 모르겠음 ..
import sys

N = int(sys.stdin.readline())
dp = [0 for _ in range(100001)]
dp[0] = 1
dp[1] = 3
dp[2] = 7

for i in range(3, N+1):
    dp[i] = (dp[i-1]*2+dp[i-2])%9901

print(dp[N])