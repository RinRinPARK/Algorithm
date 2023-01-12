import sys

N = int(sys.stdin.readline())

if N < 100:
    print(N)
else:
    count = 99
    for i in range(100, N+1):
        a = list(str(i))
        a = list(map(int, a))
        if (a[1]-a[0]) == (a[2]-a[1]):
            count += 1
    print(count)
