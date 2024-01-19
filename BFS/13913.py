import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
queue = deque()
queue.append(N)
visited = [0 for _ in range(100001)]
cnt = [0 for _ in range(100001)]

while queue:
    cur = queue.popleft()
    if cur == K:
        print(cnt[cur])
        lst = []
        i = cur
        for _ in range(cnt[cur] + 1):
            lst.append(cur)
            cur = visited[cur]
        print(' '.join(map(str, lst[::-1])))
        exit()

    for ncur in (cur+1, cur-1, cur*2):
        if (0 <= ncur < 100001) and (cnt[ncur] == 0):
            queue.append(ncur)
            visited[ncur] = cur
            cnt[ncur] = cnt[cur] + 1