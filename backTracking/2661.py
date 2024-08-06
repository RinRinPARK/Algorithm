import sys

N = int(sys.stdin.readline())
nums = ['1','2','3']

def check(s):
    l = len(s)
    for idx in range(l-1, -1, -1):
        tmp = s[idx:l]
        if len(tmp) * 2 <= len(s):
            if tmp == s[idx-len(tmp):idx]:
                return False
        else:
            return True

def dfs(d, s):
    if d == N:
        print(s)
        return True

    for i in nums:
        # 넣어도 되는지 확인
        if check(s + i):
            if dfs(d+1, s+i):
                return True

    return False

dfs(0, "")
