import sys

H, W = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))
answer = 0

for i in range(1, W-1):
    max_left = max(heights[:i])
    max_right = max(heights[i+1:])

    if (max_left > heights[i]) and (max_right > heights[i]):
        answer += (min(max_left, max_right) - heights[i])

print(answer)