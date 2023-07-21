
"""

힙큐를 이용해 부르트포스로 풀었는데 자꾸 시간초과가 남.
다중 반복문이라 그런 것 같긴 한데,
도저히 시간복잡도를 줄일 방법이 떠오르지 않음.  ㅠㅠ
"""

import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

for i in range(N):
    for j in range(M):
        heap = []
        visited = [[0 for _ in range(M)] for _ in range(N)]
        count = 0
        value = 0
        heapq.heappush(heap, [-graph[i][j], i, j])
        while count < 4:
            val, x, y = heapq.heappop(heap)
            visited[x][y] = 1
            count += 1
            value -= val
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if (0 <= nx < N) and (0 <= ny < M) and (visited[nx][ny] == 0):
                    heapq.heappush(heap, [-graph[nx][ny], nx, ny])
        result = max(result, value)

print(result)
