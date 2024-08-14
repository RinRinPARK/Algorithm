import sys

M, N = map(int, sys.stdin.readline().split())
ans = []

def isPrime(n):
    if n == 1:
        return False
    
    num = int(n ** (1/2))

    for i in range(2, num+1):
        if n % i == 0:
            return False
        
    return True

for a in range(M, N+1):
    if isPrime(a):
        ans.append(a)

for x in ans:
    print(x)