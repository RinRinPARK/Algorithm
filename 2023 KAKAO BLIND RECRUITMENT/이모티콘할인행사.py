# LV.2
# bruteForce

# 1. 이모티콘 플러스 서비스 가입자를 최대한 늘리는 것.
# 2. 이모티콘 판매액을 최대한 늘리는 것.
# users: n명의 구매기준 2차원 배열[비율, 가격]
# emoticons: m개의 이모티콘 정가 1차원 배열
# answers:  플러스 서비스 가입 수와 이모티콘 매출액
from itertools import product
def solution(users, emoticons):
    sales = [10,20,30,40]
    candidates = product(sales, repeat = len(emoticons))
    result_sub = 0
    result_take = 0
    
    for candidate in candidates:
        e = []
        new_sub = 0
        new_take = 0
        for i in range(len(candidate)):
            e.append([candidate[i], emoticons[i]*((100-candidate[i])/100)])
        for j in range(len(users)):
            pers_take = 0
            for rate,cost in e:
                if rate >= users[j][0]:
                    pers_take += cost
            if pers_take >= users[j][1]:
                new_sub += 1
            else:
                new_take += pers_take
        if new_sub > result_sub:
            result_sub = new_sub
            result_take = new_take
        elif new_sub == result_sub:
            result_take = max(result_take, new_take)
    
    answer = [result_sub, result_take]
    
    return answer
