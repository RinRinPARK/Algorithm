import sys

N, M = map(int, sys.stdin.readline().split())
A = []
B = []
result = []

for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

M , K = map(int, sys.stdin.readline().split())
for _ in range(M):
    B.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(K):
        val = 0
        for c in range(M):
            val += (A[i][c] * B[c][j])
        result.append(val)
            

for n in range(len(result)):
    print(result[n], end = ' ')
    if -((n+1) % K == 0):
        print()

        