import sys

def check(a,b,s):
    a = int(a)
    if s == "<":
        return a < b
    else:
        return a > b

def dfs(n, selected):

    if n == k + 1:
        result.append(selected)
        return 
    
    for i in range(9, -1, -1):
        if (n == 0) or ((visited[i] != 1) and (check(selected[-1],i,bracket[n-1]))):
            visited[i] = 1
            dfs(n+1, selected+str(i))
            visited[i] = 0

k = int(sys.stdin.readline())
bracket = list(sys.stdin.readline().replace(" ", ""))
visited = [0 for _ in range(10)]
result = []
dfs(0, "")

result.sort()

print(result[-1])
print(result[0])