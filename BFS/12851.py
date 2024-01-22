import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
cnt = [float("inf") for _ in range(100001)]
queue = deque()
queue.append(N)
cnt[N] = 0
result = float("inf")
result_mv = 0

while queue:
    n = queue.popleft()
    if n == K:
        if result > cnt[n]:
            result = cnt[n]
            result_mv = 1
        elif result == cnt[n]:
            result_mv += 1
        continue

    for p in (n+1, n-1, n*2):
        if (0 <= p < 100001):
            if cnt[p] >= cnt[n] + 1:
                cnt[p] = cnt[n] + 1
                queue.append(p)

print(result)
print(result_mv)