import sys
lst = [0]*101
lst[1] = 1
lst[2] = 1
lst[3] = 1
lst[4] = 2
lst[5] = 2

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    if N < 6:
        print(lst[N])
    else:
        for i in range(6, N+1):
            lst[i] = lst[i-5]+lst[i-1]
        print(lst[N])
