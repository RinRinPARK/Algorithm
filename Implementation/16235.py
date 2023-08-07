import sys

N, M, K = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
farm = [[5 for _ in range(N)] for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    trees[x-1][y-1].append(z)

for _ in range(K):
    new_trees = [[[] for _ in range(N)] for _ in range(N)]

    # 봄과 여름 ( + 가을 번식 부분 처리)
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                trees[i][j].sort()
                dead = 0
                new_tree_list = []
                for age in trees[i][j]:
                    if farm[i][j] >= age:
                        farm[i][j] -= age
                        new_age = age + 1
                        new_tree_list.append(new_age)
                        if new_age % 5 == 0:
                            for k in range(8):
                                nx = i + dx[k]
                                ny = j + dy[k]
                                if 0 <= nx < N and 0 <= ny < N:
                                    new_trees[nx][ny].append(1)
                    else:
                        dead += age // 2
                farm[i][j] += dead
                trees[i][j] = new_tree_list

    # 가을
    for i in range(N):
        for j in range(N):
            if new_trees[i][j]:
                trees[i][j].extend(new_trees[i][j])

    # 겨울
    for i in range(N):
        for j in range(N):
            farm[i][j] += A[i][j]

ans = sum(len(trees[i][j]) for i in range(N) for j in range(N))
print(ans)
