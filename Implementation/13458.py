import sys
import math

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())
count = 0

for people in lst:
    count += 1
    people -= B
    if people > 0:
        count += math.ceil(people / C)

print(count)
