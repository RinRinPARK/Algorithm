import sys

X = int(sys.stdin.readline())
a = [0]*(X+1)

for i in range(2, X+1):
    a[i] = a[i-1]+1
    if i % 3 == 0:
        a[i] = min(a[i], a[i//3]+1)
    if i % 2 == 0:
        a[i] = min(a[i], a[i//2]+1)

print(a[X])
