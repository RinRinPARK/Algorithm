import sys

N, M = map(int, sys.stdin.readline().split())
lst = []
result = []

for _ in range(N):
    lst.append(list(sys.stdin.readline().rstrip()))

for i in range(N-7):
    for j in range(M-7):
        w = 0
        b = 0
        for m in range(i, i+8):
            for n in range(j, j+8):
                if (m+n) % 2 == 0:
                    if lst[m][n] == "W":
                        w += 1
                    else:
                        b += 1
                else:
                    if lst[m][n] == "B":
                        w += 1
                    else:
                        b += 1
        result.append(w)
        result.append(b)

print(min(result))
