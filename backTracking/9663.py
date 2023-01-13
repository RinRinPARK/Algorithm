import sys

N = int(sys.stdin.readline())
col = [0]*N
count = 0


def promising(n):
    for i in range(n):
        if (col[n] == col[i]) or (abs(col[n]-col[i]) == abs(n-i)):
            return False
    return True


def nQueens(n):
    global count
    if n == N:
        count += 1
    else:
        for j in range(N):
            col[n] = j
            if (promising(n)):
                nQueens(n+1)


nQueens(0)
print(count)
