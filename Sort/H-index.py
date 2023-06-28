def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)):
        val = len(citations)-i
        if (val <= citations[i]):
            answer = val
            break
    return answer
