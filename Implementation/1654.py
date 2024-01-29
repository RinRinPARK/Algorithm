# N개보다 많이 만드는 것도 N개를 만드는 것에 포함
# 항상 K ≦ N
import sys

K, N = map(int, sys.stdin.readline().split())
lines = []
for _ in range(K):
    lines.append(int(sys.stdin.readline()))
mid = max(lines)//2
left = 1
right = max(lines)

while left <= right:
    mid = (left + right) // 2
    s = 0
    for line in lines:
        s += line // mid
    if s >= N:
        left = mid + 1
        mid = (left + right) // 2
    elif s < N:
        right = mid - 1
        mid = (left + right) // 2

print(right)

"""
# 시간초과 bruteForce 코드
if K == N:
    print(min(lines))
    exit()

for i in range(max(lines), 0, -1):
    s = 0
    for line in lines:
        s += line // i
    
    if s >= N:
        print(i)
        exit()
"""