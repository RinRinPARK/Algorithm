import sys

# 위치를 옮기는 아이들의 수를 최소
# N명의 아이들이 임의의 순서로 줄을 서 있을 때, 번호 순서대로 배치하기 위해 옮겨지는 아이의 최소 수
N = int(sys.stdin.readline())
kids = [int(sys.stdin.readline()) for _ in range(N)]
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if kids[j] < kids[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(N-max(dp))