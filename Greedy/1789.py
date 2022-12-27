import sys

S = int(sys.stdin.readline())
N = 0
i = 1

while N <= S:
    N = N+i
    i += 1

print(i-2)
