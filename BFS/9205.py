import sys
from collections import deque

# 맥주가 20개
# 50미터에 한 병씩 마심
# 박스에 들어있는 맥주는 20병을 넘을 수 없다

# 행복하게 페스티벌에 갈 수 있으면 "happy", 중간에 맥주가 바닥나서 더 이동할 수 없으면 "sad"를 출력
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())

    sang = list(map(int,sys.stdin.readline().split())) # 상근이 집
    store = [] # 편의점
    for _ in range(n):
        store.append(list(map(int,sys.stdin.readline().split())))
    festival = list(map(int,sys.stdin.readline().split())) # 펜타포트

    visited = [0 for _ in range(n)]

    queue = deque()
    queue.append(sang)

    flag = 0
    while queue:
        x, y = queue.popleft()

        dist = abs(x - festival[0]) + abs(y - festival[1])

        if dist <= 1000:
            print("happy")
            flag = 1
            break

        for i in range(n):
            if (visited[i] == 0) and (abs(x - store[i][0]) + abs(y - store[i][1]) <= 1000):
                queue.append([store[i][0], store[i][1]])
                visited[i] = 1

    if flag == 0:
        print("sad")



