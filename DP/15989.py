import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())

    dp = [1 for _ in range(n + 1)]

    for i in range(2, n + 1):
        dp[i] += dp[i-2]

    for i in range(3, n + 1):
        dp[i] += dp[i-3]

    print(dp[n])




"""
시간초과 backtracking

import sys

def dfs(n, visited, curr):
    if curr > n:
        return

    if curr == n:
        cnt = [0, 0, 0]
        for k in visited:
            cnt[k - 1] += 1
        answer.add(str(cnt))
        return

    for i in [1,2,3]:
        visited.append(i)
        dfs(n, visited, curr + i)
        visited.pop()

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    answer = set()
    dfs(n, [], 0)

    print(len(answer))
"""