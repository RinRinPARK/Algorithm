import sys

N = int(sys.stdin.readline())
lst = [[0 for _ in range(10)] for _ in range(N+1)]
for i in range(1, 10):
    lst[1][i] = 1

for m in range(2, N+1):
    for n in range(10):
        if n == 0:
            lst[m][n] = lst[m-1][1]
        elif n == 9:
            lst[m][n] = lst[m-1][8]
        else:
            lst[m][n] = lst[m-1][n-1]+lst[m-1][n+1]

print(sum(lst[N]) % 1000000000)
