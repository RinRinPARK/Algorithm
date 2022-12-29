import sys

n = int(sys.stdin.readline())
fib = [0]*(n+1)
fib[1] = 1

for i in range(2, n+1):
    fib[i] = fib[i-2]+fib[i-1]

print(fib[n])
