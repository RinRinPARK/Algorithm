import sys

N = int(sys.stdin.readline())
values = [int(sys.stdin.readline())]

if N == 1:
    print(values[0])

else:
    for _ in range(N-1):
        values.append(list(map(int, sys.stdin.readline().split())))

    values[1][0] = values[0]+values[1][0]
    values[1][1] = values[0]+values[1][1]

    for i in range(2, N):
        for j in range(len(values[i])):
            if j == 0:
                values[i][j] = values[i-1][j]+values[i][j]
            elif j == len(values[i])-1:
                values[i][j] = values[i-1][j-1]+values[i][j]
            else:
                values[i][j] = max(values[i-1][j-1]+values[i][j],
                                   values[i-1][j]+values[i][j])

    print(max(values[N-1]))
