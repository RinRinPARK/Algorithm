def solution(participant, completion):
    answer = ''
    dict = {}
    for person in participant:
        if person in dict:
            dict[person] += 1
        else:
            dict[person] = 1
    for comple in completion:
        dict[comple] -= 1
    answer = max(dict, key=dict.get)
    return answer
