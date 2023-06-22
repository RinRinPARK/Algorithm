def solution(progresses, speeds):
    answer = []
    lst = []

    for i in range(len(speeds)):
        day = (100-progresses[i])//speeds[i]
        if ((100-progresses[i]) % speeds[i]) != 0:
            day += 1
        lst.append(day)

    i = 0
    j = 1
    count = 1
    while j < len(lst):
        if (lst[j] <= lst[i]) and (j != i):
            count += 1
            j += 1
        else:
            answer.append(count)
            count = 1
            i = j
            j += 1
    answer.append(count)

    return answer
