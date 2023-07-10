"""
union-find로 푼 풀이!

def union(root, a, b):
    x = find(root, a)
    y = find(root, b)
    if x > y:
        root[x] = y
    else:
        root[y] = x


def find(root, a):
    if root[a] == a:
        return a
    root[a] = find(root, root[a])
    return root[a]


def solution(n, computers):
    answer = 0
    root = [k for k in range(n)]

    for i in range(n):
        for j in range(n):
            if (computers[i][j] == 1):
                union(root, i, j)
    for i in range(n):
        find(root, i)
    answer = len(set(root))

    return answer
"""

# BFS를 이용한 풀이!
from collections import deque


def BFS(queue, n, visited, computers, arr):
    queue.append(arr)

    while queue:
        lst = queue.popleft()
        for k in range(n):
            if (lst[k] == 1) and (visited[k] == 0):
                visited[k] = 1
                queue.append(computers[k])


def solution(n, computers):
    answer = 0
    queue = deque()
    visited = [0 for _ in range(n)]

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            answer += 1
            BFS(queue, n, visited, computers, computers[i])

    return answer
