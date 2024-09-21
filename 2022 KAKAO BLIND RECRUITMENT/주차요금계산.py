# 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return

def calculate(i, o):
    
    intime = int(i[:2]) * 60 + int(i[3:])
    outtime = int(o[:2]) * 60 + int(o[3:])
    
    return outtime - intime
    

def solution(fees, records):
    answer = []
    
    t, tf = fees[0], fees[1]
    p, pf = fees[2], fees[3]
    
    find = {}
    total = {}
    garage = []
    
    for record in records:
        time, car, state = record.split(' ')
        
        if state == 'IN':
            find[car] = time
            garage.append(car)
            
        else:
            garage.remove(car)
            
            # 총시간 계산
            tminute = calculate(find[car], time)
            
            if car in total.keys():
                total[car] += tminute
            else:
                total[car] = tminute
                
                
    # 아직 안나간 차
    if len(garage) > 0:
        for c in garage:
            m = calculate(find[c], '23:59')
            
            if c in total.keys():
                total[c] += m
            else:
                total[c] = m
                
    ans = []
    
    for a in total.keys():
        ans.append([a, total[a]])
        
    ans.sort(key = lambda x: x[0])
    
    # 요금 계산
    for a, b in ans:
        b -= t
        result = tf
        
        if b > 0:
            if b % p != 0:
                result += ((b // p + 1) * pf)
            else:
                result += ((b // p) * pf)
                
        answer.append(result)

    return answer