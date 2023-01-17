import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
oprt = list(map(int, sys.stdin.readline().split()))

maxi = float("-inf")
mini = float("inf")


def dfs(count, result, plus, minus, multiply, division):
    global maxi, mini
    if count == N:
        maxi = max(result, maxi)
        mini = min(result, mini)
    if plus:
        dfs(count+1, result+num[count], plus-1, minus, multiply, division)
    if minus:
        dfs(count+1, result-num[count], plus, minus-1, multiply, division)
    if multiply:
        dfs(count+1, result*num[count], plus, minus, multiply-1, division)
    if division:
        dfs(count+1, int(result/num[count]), plus, minus, multiply, division-1)


dfs(1, num[0], oprt[0], oprt[1], oprt[2], oprt[3])
print(maxi)
print(mini)
