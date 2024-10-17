import sys

S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

def dfs(curr):
    if len(curr) == len(S):
        if curr == S:
            print(1)
            exit()

    if len(curr) == 0:
        return

    if curr[0] == 'B':
        dfs(curr[1:][::-1])
    if curr[-1] == 'A':
        dfs(curr[:-1])


dfs(T)

print(0)


"""
시간 초과

import sys

S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()


def dfs(curr):

    if len(curr) > len(T):
        return
    
    if len(curr) == len(T):
        if (curr == T):
            print(1)
            exit()

    for m in ['A', 'B']:
        if (len(curr) + 1) > len(T):
            return
        if m == 'A':
            dfs(curr + 'A')

        else:
            new = curr + 'B'
            dfs(new[::-1])

dfs('')
print(0)

"""