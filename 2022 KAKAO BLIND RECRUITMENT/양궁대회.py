# 현재 상황은 어피치가 화살 n발을 다 쏜 후이고 라이언이 화살을 쏠 차례

def calculate(apeach, lions):
    
    a, l = 0, 0
    
    for x in range(11):
        if apeach[x] or lions[x]:
            if apeach[x] >= lions[x]:
                a += (10-x)
            else:
                l += (10-x)
    return l - a

def dfs(num, apeach, lions, cnt, n):
    global maxdiff, answer
    
    if cnt == n:
        score = calculate(apeach, lions)
        
        if score > maxdiff:
            maxdiff = score
            answer = lions[:]
        
        # 가장 낮은 점수를 더 많이 맞춘 경우
        if score == maxdiff:
            for p in range(10, -1, -1):
                if (lions[p] != answer[p]):
                    if lions[p] > answer[p]:
                        answer = lions[:]
                    break
        
        return
    
    for j in range(num+1, 11):
        
        for k in range(1, n-cnt+1):
            if cnt + k <= n:
                lions[j] = k
                dfs(j, apeach, lions, cnt + k, n)
                lions[j] = 0
    

maxdiff = 0
answer = [0 for _ in range(11)]
def solution(n, info):
    global maxdiff, answer
    
    if n == 1:
        return [-1]
    
    for i in range(11):
        lions = [0 for _ in range(11)]
        lions[i] = info[i] + 1
        dfs(i, info, lions, lions[i], n)
        
    if maxdiff == 0:
        return [-1]
    else:
        return answer