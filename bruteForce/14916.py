"""
# 무지성 시간초과 코드

# 1
import sys
from itertools import combinations_with_replacement

n = int(sys.stdin.readline())

for i in range(n):
    lsts = combinations_with_replacement([5,2], i)
    for lst in lsts:
        if sum(lst) == n:
            print(i)
            exit()

print(-1)

# 2(정답이긴 한데, 시간복잡도가 n^2인 코드)
import sys

n = int(sys.stdin.readline())
result = float("inf")

for i in range(n//5+1):
    for j in range(n//2+1):
        if (5*i + 2*j) == n:
            result = min(result, i+j)

if result == float("inf"):
    print(-1)
else:
    print(result)

"""

import sys

n = int(sys.stdin.readline())
result = float("inf")

for i in range(n//5+1):

    if (n - 5*i) % 2 == 0:
        result = min(result, i + ((n - 5*i) // 2))

if result == float("inf"):
    print(-1)
else:
    print(result)
