import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    dp = [0 for _ in range(M+1)]
    dp[0] = 1

    for coin in coins:
        for amount in range(coin, M+1):
            dp[amount] += dp[amount - coin]

    print(dp[M])

"""
시간 초과 DFS

import sys
sys.setrecursionlimit(10 ** 6)

def dfs(curr, num, visited):
    global answer

    if curr == num:
        answer += 1
        return
    
    for i in range(len(coins)):
        if (curr + coins[i] <= num):
            visited[i] += 1
            if (str(visited) not in dp[curr + coins[i]]):
                dp[curr + coins[i]].append(str(visited))
                dfs(curr + coins[i], num, visited)
            visited[i] -= 1

    return

# 동전의 종류가 주어질 때에 주어진 금액을 만드는 모든 방법
T = int(sys.stdin.readline())
for _ in range(T):
    answer = 0
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    dp = [[] for _ in range(M + 1)]
    dfs(0, M, [0 for _ in range(N)])

    print(answer)
"""