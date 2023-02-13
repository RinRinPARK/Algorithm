import sys
sys.setrecursionlimit(10**6)

X, Y, W, S = map(int, sys.stdin.readline().split())

a = (X+Y)*W
if (X+Y) % 2 == 0:
    b = max(X, Y)*S
else:
    b = (max(X, Y)-1)*S+W
c = min(X, Y)*S+abs(Y-X)*W

print(min(a, b, c))
