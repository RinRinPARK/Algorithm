def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        time = 0
        for j in range(i+1, len(prices)):
            time += 1
            if prices[i] > prices[j]:
                break
        answer.append(time)
    answer.append(0)
    return answer
