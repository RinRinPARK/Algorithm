import sys

# 이름이 이름인 만큼, 7명의 여학생들로 구성되어야 한다.
# 강한 결속력을 위해, 7명의 자리는 서로 가로나 세로로 반드시 인접해 있어야 한다.
# 화합과 번영을 위해, 반드시 ‘이다솜파’의 학생들로만 구성될 필요는 없다.
# 7명의 학생 중 ‘이다솜파’의 학생이 적어도 4명 이상은 반드시 포함되어 있어야 한다.

# 여학생반의 자리 배치도가 주어졌을 때, ‘소문난 칠공주’를 결성할 수 있는 모든 경우의 수
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

students = []
for _ in range(5):
    students.append(list(sys.stdin.readline().strip()))
answer = set()
visit = [[0 for _ in range(5)] for _ in range(5)]
def dfs(visited, spa, ypa):

    if ypa > 3:
        return

    if (spa + ypa) == 7:
        visited.sort()
        answer.add(str(visited))
        return

    for x, y in visited:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if (0 <= nx < 5) and (0 <= ny < 5) and (visit[nx][ny] == 0):
                visit[nx][ny] = 1
                if students[nx][ny] == 'Y':
                    dfs(visited+[[nx, ny]], spa, ypa + 1)
                else:
                    dfs(visited+[[nx, ny]], spa + 1, ypa)
                visit[nx][ny] = 0

for i in range(5):
    for j in range(5):
        visit[i][j] = 1
        if students[i][j] == 'Y':
            dfs([[i, j]], 0, 1)
        else:
            dfs([[i, j]], 1, 0)
        visit[i][j] = 0

print(len(answer))