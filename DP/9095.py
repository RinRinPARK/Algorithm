import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = [0, 1, 2, 4]

    if n < 4:
        print(a[n])
    else:
        for i in range(4, n+1):
            a.append(a[i-3]+a[i-2]+a[i-1])
        print(a[n])
