import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

left, right = 0, 0
accumulate = 0
answer = float("inf")

while True:
    if accumulate >= S:
        answer = min(answer, right - left)
        accumulate -= nums[left]
        left += 1
    elif right == N:
        break
    else:
        accumulate += nums[right]
        right += 1

if answer == float("inf"):
    print(0)
else:
    print(answer)

"""
시간초과
import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

dp = [[0,0] for _ in range(N)]
answer = float("inf")

for i in range(N-1):
    curr_inc = i
    accum_inc = nums[i]
    curr_dec = i
    accum_dec = nums[i]
    for j in range(i+1, N):
        if j == (curr_inc + 1):
            curr_inc += 1
            dp[i][0] += 1
            accum_inc += nums[j]
        if j == (curr_dec - 1):
            curr_dec -= 1
            dp[i][1] += 1
            accum_dec += nums[j]

    if accum_inc > S:
        answer = min(answer, dp[i][0])

    if accum_dec > S:
        answer = min(answer, dp[i][1])

print(answer)

"""