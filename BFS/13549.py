import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
moved = [0 for _ in range(100001)]
cnt = [float("inf") for _ in range(100001)]
queue = deque()
queue.append(N)
cnt[N] = 0
result = float("inf")

while queue:
    n = queue.popleft()
    if n == K:
        result = min(cnt[n], result)
        continue
    for p in (n+1, n-1, n*2):
        if (0<=p<100001):
            if p == n*2:
                if cnt[p] > cnt[n]:
                    cnt[p] = cnt[n]
                    moved[p] = n
                    queue.append(p)
            else:            
                if cnt[p] > cnt[n]+1:
                    cnt[p] = cnt[n]+1
                    moved[p] = n
                    queue.append(p)

print(result)
