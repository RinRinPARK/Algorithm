def solution(brown, yellow):
    answer = []
    candidate = []

    # yellow의 약수들 [x,y]을 구하고 얘네를 candidate
    # ((x+2)*(y+2))-yellow가 brown값이랑 같으면 answer로
    # answer에서 sort(reverse=True)

    for i in range(1, yellow+1):
        if yellow % i == 0:
            candidate.append([i, yellow//i])

    for ele in candidate:
        if brown == ((ele[0]+2)*(ele[1]+2)-yellow):
            ele[0] += 2
            ele[1] += 2
            answer = sorted(ele, reverse=True)

    return answer
