import sys

# 집에 공유기 C개를 설치
# 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치

# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대
N, C = map(int, sys.stdin.readline().split())
house = []
for _ in range(N):
    house.append(int(sys.stdin.readline()))
house.sort()
start = 1
end = house[-1] - house[0]

answer = 0
while start <= end:
    mid = (start + end) // 2

    now = house[0]
    count = 1

    for i in range(1, N):
        if house[i] >= mid + now:
            now = house[i]
            count += 1

    if count >= C:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)



"""
메모리 초과 ^^..

import sys
sys.setrecursionlimit(10**6)

# 집에 공유기 C개를 설치
# 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치

# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대
N, C = map(int, sys.stdin.readline().split())
house = []
for _ in range(N):
    house.append(int(sys.stdin.readline()))

house.sort()
answer = 0
def dfs(num, visited):
    global answer

    if len(visited) == C:
        dists = []
        for x in range(C-1):
            dists.append(abs(visited[x+1] - visited[x]))

        # 가장 인접한 공유기 사이 거리
        dist = min(dists)

        answer = max(answer, dist)
        return
    
    for k in range(num + 1, N):
        dfs(k, visited + [house[k]])

for i in range(N):
    dfs(i, [house[i]])

print(answer)
"""