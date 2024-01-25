# LV.3
# backTracking + Implementaion
# n,m: 격자의 크기
# x,y: 출발위치
# r,c: 탈출지점
# k: 이동해야하는 거리
import sys

sys.setrecursionlimit(10000000)
dict = {'l': (0, -1), 'r': (0, 1), 'u': (-1, 0), 'd': (1, 0)}

def dfs(a, b, mv, r, c, k, n, m, answer):
    global find
    global result
    if (find == 1) or (mv > k) or (abs(a+1 - r) + abs(b+1 - c) + mv > k):
        return
    if mv == k:
        if a == r-1 and b == c-1:
            find = 1
            result = answer
        return
    for ele in ('d', 'l', 'r', 'u'):
        dx, dy = dict[ele]
        nx = a + dx
        ny = b + dy
        if (0 <= nx < n) and (0 <= ny < m):
            dfs(nx, ny, mv+1, r, c, k, n, m, answer + ele)

def solution(n, m, x, y, r, c, k):
    global find
    global result
    find = 0
    result = ''
    # k번 이동 안에 이동할 수 없는 거리라면 + 애초에 k번으로 이동 불가능한 거리라면
    z = k - abs(x - r) + abs(y - c)
    if z < 0 or z % 2 != 0:
        return "impossible"
    dfs(x-1, y-1, 0, r, c, k, n, m, '')
    if find == 0:
        result = "impossible"
    return result
"""
시간초과 bruteForce 코드

from itertools import product

def solution(n, m, x, y, r, c, k):
    answer = ''
    mv = ['l', 'r', 'u', 'd']
    dict = {'l':(0,-1), 'r':(0, 1), 'u':(-1,0), 'd':(1,0)}
    
    lsts = list(product(mv, repeat = k))
    lsts.sort()
    
    for lst in lsts:
        flag = 0
        a = x-1
        b = y-1
        for ele in lst:
            dx, dy = dict[ele]
            nx = a + dx
            ny = b + dy
            if (0<=nx<n) and (0<=ny<m):
                a = nx
                b = ny
            else:
                flag = 1
                break
        if (flag == 0) and (a == r-1) and (b == c-1):
            answer = ''.join(lst)
            break
    if answer == '':
        answer = "impossible"
    return answer
"""