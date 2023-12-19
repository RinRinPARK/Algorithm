import sys
from itertools import combinations
#  최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음

L, C = map(int,sys.stdin.readline().split())
chars = list(map(str, sys.stdin.readline().split()))

arrs = map(list, combinations(chars, L))
results = []
moum = ['a','e','i','o','u']

for arr in arrs:
    ja = 0
    mo = 0    
    new = sorted(arr)
    for char in new:
        if char in moum:
            mo += 1
        else:
            ja+=1
    if (ja>=2 and mo >=1):
        results.append("".join(new))

results.sort()
for result in results:
    print(result)
