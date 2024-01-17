import sys

# 민규는 돈을 최대한 "많이" 지불해서 카드 N개 구매. 
# 카드가 i개 포함된 카드팩의 가격은 Pi원이다.
N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N+1)]

# i를 만들어야 하고
for i in range(1, N+1):
    # j를 이용해서
    for j in range(1, i+1):
        dp[i] = max(dp[i], P[j-1]+dp[i-j])
print(dp[N])