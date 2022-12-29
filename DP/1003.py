import sys

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    a = [[0, 0]]*(N+1)

    for i in range(N+1):
        if i == 0:
            a[0] = [1, 0]
        elif i == 1:
            a[1] = [0, 1]
        else:
            a[i] = [a[i-2][0]+a[i-1][0], a[i-2][1]+a[i-1][1]]

    print(a[N][0], a[N][1])
