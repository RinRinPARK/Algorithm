import sys

A, B = map(int, sys.stdin.readline().split())
count = 0

while (B != A):
    if B < A:
        count = -2
        break
    elif B % 2 == 0:
        B = B//2
        count += 1
    elif str(B)[-1] == "1":
        B = str(B)[:-1]
        B = int(B)
        count += 1
    else:
        count = -2
        break

print(count+1)
