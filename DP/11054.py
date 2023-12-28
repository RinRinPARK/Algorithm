"""
시간 초과 코드 

import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
dp1 = [0 for _ in range(N)]
dp2 = [0 for _ in range(N)]
lst1 = []
lst2 = []
 
# 오름차순 수열 찾고, 내림차순 수열 찾아서 연결하기

# 오름차순
for i in range(N):
    for j in range(i):
        if (A[i] > A[j]) and (dp1[i] < dp1[j]):
            dp1[i] = dp1[j]
            lst1.append([i, dp1[i]])
    
    dp1[i]+=1

# 내림차순
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if (A[i] > A[j]) and (dp2[i] < dp2[j]):
            dp2[i] = dp2[j]
            lst2.append([i, dp2[i]])

    dp2[i] += 1

# 합치기
result = []

for a, val1 in lst1:
    for b, val2 in lst2:
        if (a == b):
            result.append(val1+val2)

print(max(result)+1)

"""

import sys
import copy

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
A_reverse = copy.deepcopy(A)
A_reverse.reverse()
dp1 = [0 for _ in range(N)]
dp2 = [0 for _ in range(N)]
 
# 오름차순 수열 찾고, 내림차순 수열 찾아서 연결하기

# 오름차순 + 내림차순
for i in range(N):
    for j in range(i):
        if (A[i] > A[j]) and (dp1[i] < dp1[j]):
            dp1[i] = dp1[j]
        if (A_reverse[i] > A_reverse[j]) and (dp2[i] < dp2[j]):
            dp2[i] = dp2[j]
    
    dp1[i] += 1
    dp2[i] += 1

# 합치기
result = []

for k in range(N):
    result.append(dp1[k] + dp2[N-k-1]-1)

print(max(result))