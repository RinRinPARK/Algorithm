"""
# Bruteforce로 무지성 풀이

import sys
from collections import deque

graph = []
queue = deque()
for i in range(9):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(9):
        if lst[j] == 0:
            queue.append([i,j])

    graph.append(lst)

def rowFind(x, y):
    # 0이 1개 이상이라서 한번에 빈칸의 값을 찾을 수 없으면 -1 반환
    if graph[x].count(0) > 1:
        return -1
    
    lst = graph[x][:]
    lst.sort()
    for k in range(9):
        if lst[k] != k:
            return k
        
    return 9

def colFind(x, y):
    lst = []
    for p in range(9):
        lst.append(graph[p][y])

    # 0이 1개 이상이라서 한번에 빈칸의 값을 찾을 수 없으면 -1 반환
    if lst.count(0) > 1:
        return -1
    
    lst.sort()
    for k in range(9):
        if lst[k] != k:
            return k
        
    return 9

def blockFind(x, y):

    # 1블록: 0 <= x < 3, 0 <= y < 3
    # 2블록: 0 <= x < 3, 3 <= y < 6
    # 3블록: 0 <= x < 3, 6 <= y < 9
    # 4블록: 3 <= x < 6, 0 <= y < 3
    # 5블록: 3 <= x < 6, 3 <= y < 6
    # 6블록: 3 <= x < 6, 6 <= y < 9
    # 7블록: 6 <= x < 9, 0 <= y < 3
    # 8블록: 6 <= x < 9, 3 <= y < 6
    # 9블록: 6 <= x < 9, 6 <= y < 9
    lst = []

    if (0 <= x < 3):
        if (0 <= y < 3):
            for i in range(3):
                for j in range(3):
                    lst.append(graph[i][j])
        elif (3 <= y < 6):
            for i in range(3):
                for j in range(3, 6):
                    lst.append(graph[i][j])
        else:
            for i in range(3):
                for j in range(6,9):
                    lst.append(graph[i][j])
    elif (3 <= x < 6):
        if (0 <= y < 3):
            for i in range(3, 6):
                for j in range(3):
                    lst.append(graph[i][j])
        elif (3 <= y < 6):
            for i in range(3, 6):
                for j in range(3, 6):
                    lst.append(graph[i][j])
        else:
            for i in range(3, 6):
                for j in range(6, 9):
                    lst.append(graph[i][j])
    else:
        if (0 <= y < 3):
            for i in range(6, 9):
                for j in range(3):
                    lst.append(graph[i][j])
        elif (3 <= y < 6):
            for i in range(6, 9):
                for j in range(3, 6):
                    lst.append(graph[i][j])
        else:
            for i in range(6, 9):
                for j in range(6, 9):
                    lst.append(graph[i][j])

    # 0이 1개 이상이라서 한번에 빈칸의 값을 찾을 수 없으면 -1 반환
    if lst.count(0) > 1:
        return -1
    
    lst.sort()
    for k in range(9):
        if lst[k] != k:
            return k
        
    return 9


while queue:
    x, y = queue.popleft()

    # 가로줄 살펴보기
    row_result = rowFind(x, y)
    if row_result != -1:
        graph[x][y] = row_result
        continue

    # 세로줄 살펴보기
    col_result = colFind(x, y)
    if col_result != -1:
        graph[x][y] = col_result
        continue

    # 블록 내부 살펴보기
    block_result = blockFind(x, y)
    if block_result != -1:
        graph[x][y] = block_result
        continue

    # 그래도 못찾으면 queue에 다시 append
    queue.append([x,y])

for v in graph:
    print(*v)
"""

import sys

graph = []
find_lst = []
for i in range(9):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(9):
        if lst[j] == 0:
            find_lst.append([i,j])

    graph.append(lst)


def rowFind(x, i):
    # 중복되는 숫자가 없으면
    for k in graph[x]:
        if k == i:
            return False
        
    return  True

def colFind(y, i):

    for k in range(9):
        if graph[k][y] == i:
            return False
        
    return  True

def blockFind(x, y, i):

    # 1블록: 0 <= x < 3, 0 <= y < 3
    # 2블록: 0 <= x < 3, 3 <= y < 6
    # 3블록: 0 <= x < 3, 6 <= y < 9
    # 4블록: 3 <= x < 6, 0 <= y < 3
    # 5블록: 3 <= x < 6, 3 <= y < 6
    # 6블록: 3 <= x < 6, 6 <= y < 9
    # 7블록: 6 <= x < 9, 0 <= y < 3
    # 8블록: 6 <= x < 9, 3 <= y < 6
    # 9블록: 6 <= x < 9, 6 <= y < 9

    nx = x//3 * 3
    ny = y//3 * 3
    for m in range(3):
        for n in range(3):
            if graph[nx+m][ny+n] == i:
                return False
    return True

def dfs(n):

    if n == len(find_lst):
        for g in graph:
            print(*g)
        exit()

    x = find_lst[n][0]
    y = find_lst[n][1]

    for i in range(1, 10):
        if (rowFind(x,i)) and (colFind(y, i)) and (blockFind(x,y,i)):
            graph[x][y] = i
            dfs(n+1)
            graph[x][y] = 0


dfs(0)