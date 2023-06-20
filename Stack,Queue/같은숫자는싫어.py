def solution(arr):
    answer = []
    for ele in arr:
        if len(answer) > 0 and (ele == answer[-1]):
            continue
        else:
            answer.append(ele)
    return answer
