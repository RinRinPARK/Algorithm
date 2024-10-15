import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

# A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수
ans = 0
left = 0
right = 0


while (left <= right) and (right < len(A) + 1):
    if sum(A[left:right]) > M:
        left += 1

    elif sum(A[left:right]) < M:
        right += 1

    else:
        ans += 1
        left += 1

print(ans)

"""

시간초과 


import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

# A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수
ans = 0

for i in range(N):
    accumulate = 0
    flag = 0
    for j in range(i, N):
        if accumulate + A[j] < M:
            accumulate += A[j]
        elif accumulate + A[j] == M:
            accumulate += A[j]
            flag = 1
            break
        else:
            break
    if flag == 1:
        ans += 1

print(ans)

"""