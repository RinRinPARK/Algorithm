import sys

N = int(sys.stdin.readline())
tool = []
s = [[0 for _ in range(N+1)]]
result = []

for _ in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    lst.insert(0, 0)
    s.append(lst)


def dfs():
    if len(tool) == N//2:
        # 다 더해서 result에 더하기
        start_score = 0
        link_score = 0
        remain = list(set([j for j in range(1, N+1)]) - set(tool))
        for m in tool:
            for n in tool:
                if m == n:
                    continue
                start_score += s[m][n]
        for r in remain:
            for k in remain:
                if r == k:
                    continue
                link_score += s[r][k]
        result.append(abs(int(start_score) - int(link_score)))
    for i in range(1, N+1):
        if len(tool) == 0 or i > max(tool):
            tool.append(i)
            dfs()
            tool.pop()


dfs()
print(min(result))
