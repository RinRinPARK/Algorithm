import sys

n = int(sys.stdin.readline())
dp = [1, 3]
# 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력

for i in range(2, n):
    dp.append(dp[i-2]*2 + dp[i-1])

print(dp[n-1]%10007)