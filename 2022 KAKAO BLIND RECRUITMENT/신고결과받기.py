# 한 번에 한 명의 유저를 신고
# 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리
# k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송

# id_list: 이용자의 Id
# report: 각 이용자가 신고한 이용자의 ID정보

# 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 
def solution(id_list, report, k):
    answer = []
    
    a = {} # 유저가 신고한 유저 리스트 담는 맵
    b = {} # 신고받은 횟수 담는 맵
    
    # 배열 초기화
    for i in range(len(id_list)):
        a[id_list[i]] = []
        b[id_list[i]] = 0
    
    # 신고
    for repo in report:
        x, y = repo.split(' ')
        
        
        # 만약 신고 이력이 있다면 continue
        if y in a[x]:
            continue
            
        a[x].append(y)
        b[y] += 1
    
    # 신고 횟수 세기
    for m in range(len(id_list)):
        cnt = 0
        
        for n in a[id_list[m]]:
            if b[n] >= k:
                cnt += 1
                
        answer.append(cnt)
            
    return answer