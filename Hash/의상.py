def solution(clothes):
    answer = 1
    dict = {}
    for ele in clothes:
        if ele[1] in dict:
            dict[ele[1]] += 1
        else:
            dict[ele[1]] = 1
    for i in list(dict.values()):
        answer *= (i+1)
    answer -= 1
    return answer
