import sys

N = int(sys.stdin.readline())
lst = [0]
for _ in range(N):
    lst.append(int(sys.stdin.readline()))
answer = set()

def dfs(first, second, num):
    first.add(num)
    second.add(lst[num])

    if lst[num] in first:
        if first == second:
            answer.update(first)
            return True
        return False
    
    return dfs(first, second, lst[num])

for i in range(1, N + 1):
    if i not in answer:
        dfs(set(), set(), i)

print(len(answer))
print(*sorted(list(answer)), sep = '\n')


"""
시간초과 bruteForce backtracking

import sys

N = int(sys.stdin.readline())
first_line = [i for i in range(1, N+1)]
second_line = []

def dfs(num):

    if sum(visited) > num:
        return

    if sum(visited) == num:
        # 집합 확인
        a = set()
        b = set()
        for n in range(N):
            if visited[n] == 1:
                a.add(first_line[n])
                b.add(second_line[n])
        
        if a == b:
            print(num)
            result = list(a)
            result.sort()
            for r in result:
                print(r)
            exit()
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(num)
            visited[i] = 0



for _ in range(N):
    second_line.append(int(sys.stdin.readline()))

for k in range(N, 0, -1):
    visited = [0 for _ in range(N)]
    dfs(k)

"""