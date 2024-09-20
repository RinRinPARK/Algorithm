import math

def isPrime(num):
    if num <= 1:
        return False
    
    a = int(math.sqrt(num))
    
    for i in range(2, a + 1):
        if num % i == 0:
            return False
        
    return True

def transform(n, k):
    
    lst = []
    
    while n >= k:
        lst.append(n%k)
        n = n // k
        
    lst.append(n)
    lst.reverse()
    
    return lst
        

def solution(n, k):
    answer = 0
    
    # n을 k진수로 변경
    numk = transform(n, k)
    
    if len(numk) == 1:
        if isPrime(numk):
            return 1
        return 0
    
    loc = []
    
    # 규칙에 맞는 소수 찾기
    check = ''
    
    for i in range(len(numk)):
        
        if numk[i] == 0:
            if len(check) != 0:
                # 소수판별하고
                if isPrime(int(check)):
                    answer += 1
                # check 초기화
                check = ''
            
        else:
            check += str(numk[i])
            
    if len(check) != 0:
        if isPrime(int(check)):
            answer += 1
    
    
    return answer