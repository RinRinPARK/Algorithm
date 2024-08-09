import sys
sys.setrecursionlimit(10**6)

# 프로젝트 팀원 수에는 제한이 없다
# 혼자 하고 싶어하는 학생은 자기 자신을 선택하는 것도 가능

def dfs(i):
    global result 

    visited[i] = 1
    cycle.append(i)

    if visited[lst[i]] == 1:
        if lst[i] in cycle:
            result += len(cycle[cycle.index(lst[i]):])
            return
        return
    
    dfs(lst[i])
    


T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    lst = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [1] + [0 for _ in range(n)]
    result = 0

    for i in range(1, n+1):
        if visited[i] == 0:
            cycle = []
            dfs(i)


    print(n - result)