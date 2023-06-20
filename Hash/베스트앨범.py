def solution(genres, plays):
    answer = []
    dict = {}
    lst = []
    for i in range(len(genres)):
        lst.append([genres[i], plays[i], i])
        if genres[i] in dict:
            dict[genres[i]] += plays[i]
        else:
            dict[genres[i]] = plays[i]
    lst.sort(key=lambda x: (x[0], -x[1], x[2]))
    dict = sorted(dict.items(), key=lambda item: -item[1])
    for key in dict:
        count = 0
        for j in range(len(lst)):
            if lst[j][0] == key[0]:
                if count < 2:
                    count += 1
                    answer.append(lst[j][2])
                else:
                    break
    return answer
