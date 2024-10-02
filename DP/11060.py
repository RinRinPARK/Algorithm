import sys

# i번째 칸에 쓰여 있는 수를 Ai라고 했을 때, 
# 재환이는 Ai이하만큼 오른쪽으로 떨어진 칸으로 한 번에 점프할 수 있다

# 최소 몇 번 점프를 해야 갈 수 있는지 구하는 프로그램
# 가장 오른쪽 끝으로 갈 수 없는 경우에는 -1

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
dp = [float("inf") for _ in range(N)]
dp[0] = 0

for i in range(N):
    k = lst[i]
    for j in range(1, k+1):
        if 0 <= i + j < N:
            dp[i+j] = min(dp[i+j], dp[i] + 1)

print(dp[-1] if dp[-1] != float("inf") else -1)