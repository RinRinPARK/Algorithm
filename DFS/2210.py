import sys
from collections import deque

# 인접해 있는 네 방향으로 다섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례로 붙이면 6자리의 수
# 이동을 할 때에는 한 번 거쳤던 칸을 다시 거쳐도 되며, 
# 0으로 시작하는 000123과 같은 수로 만들 수 있다.

# 만들 수 있는 수들의 개수를 출력

dx = [ -1, 1, 0, 0]
dy = [0, 0, -1, 1]

pan = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
nums = set()

def dfs(x, y, num):

    if len(num) == 6:
        nums.add(num)
        return
    
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if (0 <= nx < 5) and (0 <= ny < 5):
            dfs(nx, ny, num+str(pan[nx][ny]))


for i in range(5):
    for j in range(5):
        dfs(i, j, str(pan[i][j]))

print(len(nums))