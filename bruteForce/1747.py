import sys
import math

N = int(sys.stdin.readline())

while True:
    word = str(N)
    flag = 0
    flag2 = 0
    if N == 1:
        N += 1
        continue

    for p in range(2, int(math.sqrt(N))+1):
        if N % p == 0:
            N += 1
            flag2 = 1
            break

    if flag2 == 1:
        continue

    for k in range(len(word)//2):
        if word[k] != word[-(k+1)]:
            flag = 1
            break

    if flag == 1:
        N += 1
        continue
    else:
        break

print(N)
