import sys

A, B, C = map(int, sys.stdin.readline().split())

def calc(A, B, C):
    if B == 1:
        return A%C
    elif B % 2 == 0:
        return calc(A, B//2, C)**2%C
    else:
        return calc(A, B//2, C)**2*A%C
    
print(calc(A, B, C))