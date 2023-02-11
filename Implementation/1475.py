import sys
import math

N = list(sys.stdin.readline().rstrip())
lst = [0]*10

for i in N:
    i = int(i)
    if i == 9:
        lst[6] += 1
    else:
        lst[i] += 1

lst[6] = math.ceil(lst[6]/2)

print(max(lst))
