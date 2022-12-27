import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    grade = []
    count = 1
    for _ in range(N):
        grade.append(list(map(int, sys.stdin.readline().split())))
    grade.sort(key=lambda x: x[0])
    rate = grade[0][1]
    for i in range(1, N):
        if grade[i][1] < rate:
            count += 1
            rate = grade[i][1]
    print(count)
