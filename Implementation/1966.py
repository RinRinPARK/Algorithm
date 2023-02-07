import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    heap = []
    N, M = map(int, sys.stdin.readline().split())
    if N == 1:
        int(sys.stdin.readline())
        print(1)
    else:
        lst = list(map(int, sys.stdin.readline().split()))
        count = 0
        queue = deque([])
        for i in range(N):
            queue.append([lst[i], i])
        while queue:
            num, order = queue.popleft()
            if (num == max(lst)) and order == M:
                print(count+1)
                queue.clear()
            elif num == max(lst):
                lst.remove(num)
                count += 1
            else:
                queue.append([num, order])
