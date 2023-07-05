def solution(number, k):
    """
    다음은 테스트 10에서 시간초과가 난 코드

    answer = ''
    pick = len(number) - k
    reserve = 0

    while len(answer) < (len(number) - k):
        val = max(number[reserve:len(number)-(pick-1)])
        answer += val
        reserve += number[reserve:len(number)-(pick-1)].index(val)+1
        pick = pick-1
        if (len(number)-reserve == pick):
            answer += number[reserve:]
            break

    return answer
    """

    answer = []
    pick = len(number) - k
    reserve = 0

    while pick > 0:
        max_val = '-1'
        max_idx = -1

        for i in range(reserve, len(number) - pick + 1):
            if number[i] > max_val:
                max_val = number[i]
                max_idx = i

            if number[i] == '9':
                break

        answer.append(max_val)
        reserve = max_idx + 1
        pick -= 1

    return ''.join(answer)
