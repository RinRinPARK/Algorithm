import sys
from collections import deque


def move(action, A):

    curr = [[0 for _ in range(2**N)] for _ in range(2**N)]
    for y in range(0, 2**N, 2**action):
        for x in range(0, 2**N, 2**action):
            for i in range(2**action):
                for j in range(2**action):
                    curr[y+j][x+(2**action)-i-1] = A[y+i][x+j]

    A = curr
    melting = []
    for a in range(2**N):
        for b in range(2**N):
            count = 0
            for k in range(4):
                nx = a + dx[k]
                ny = b + dy[k]
                if (0 <= nx < 2**N) and (0 <= ny < 2**N) and (A[nx][ny] > 0):
                    count += 1

            if count < 3:
                melting.append([a, b])

    for x, y in melting:
        A[x][y] -= 1

    return A


N, Q = map(int, sys.stdin.readline().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
A = []
for _ in range(2**N):
    A.append(list(map(int, sys.stdin.readline().split())))
actions = list(map(int, sys.stdin.readline().split()))

for action in actions:
    A = move(action, A)

visited = [[0 for _ in range(2**N)] for _ in range(2**N)]
chunk = 0
ans = 0
for m in range(2**N):
    for n in range(2**N):
        queue = deque()
        num = 0
        if (visited[m][n] == 0) and (A[m][n] != 0):
            queue.append([m, n])
            visited[m][n] = 1

        while queue:
            x, y = queue.popleft()
            ans += A[x][y]
            num += 1
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if (0 <= nx < 2**N) and (0 <= ny < 2**N) and (A[nx][ny] > 0) and (visited[nx][ny] == 0):
                    queue.append([nx, ny])
                    visited[nx][ny] = 1

        chunk = max(num, chunk)

print(ans)
print(chunk)
