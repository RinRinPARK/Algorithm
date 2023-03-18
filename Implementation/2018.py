import sys

N = int(sys.stdin.readline())
lst = [i for i in range(N+1)]
result = 0

for i in range(1, N-1):
    count = i
    for j in range(i+1, N):
        if count < N:
            count += lst[j]
        elif count == N:
            result += 1
            break
        else:
            break

print(result+1)
