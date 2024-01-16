# LV.1
# bruteForce + string(문자열)
# today - 오늘 날짜, terms - 약관 유효기간, privacies - 수집된 개인정보
# 파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return
def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    t_year = int(today[:4])
    t_month = int(today[5:7])
    t_day = int(today[8:])
    
    # 각 약관의 유효기간을 dict에 저장
    for term in terms:
        policy, period = term.split()
        term_dict[policy] = int(period)
        
    for i in range(len(privacies)):
        privacy = privacies[i]
        day, term = privacy.split()
        p = term_dict[term]
        # 유효기간 지난 날짜가 12월일 때
        if (int(day[5:7])+p)%12 == 0:
            year = int(day[:4]) + int((int(day[5:7])+p)//12)-1
            month = 12
        else:
            year = int(day[:4]) + int((int(day[5:7])+p)//12)
            month = int((int(day[5:7])+p)%12)
        if year < t_year:
            answer.append(i+1)
            continue
        if (year == t_year) and (month < t_month):
            answer.append(i+1)
            continue
        if (year == t_year) and (month == t_month) and (int(day[8:]) <= t_day):
            answer.append(i+1)
            continue
            
    return answer