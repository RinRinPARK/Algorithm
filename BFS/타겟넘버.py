def solution(numbers, target):
    answer = 0
    result = [0]

    for num in numbers:
        lst = []

        for arr in result:
            lst.append(arr + num)
            lst.append(arr - num)

        result = lst

    for count in result:
        if count == target:
            answer += 1

    return answer
