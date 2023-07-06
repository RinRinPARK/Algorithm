def solution(people, limit):
    """
    다음은 효율성검사에서 시간초과가 난 코드
    answer = 0
    people.sort()

    # 한번 움직일 때 최대한 많은 사람 태워서 이동해야함
    for i in range(len(people)-1, -1, -1):
        if people[i] == 0:
            continue
        weight = people[i]
        for j in range(0, i):
            if people[j] == 0:
                continue
            if weight+people[j] <= limit:
                weight += people[j]
                people[j] = 0
            else:
                break
        answer += 1

    return answer
    """

    """
    위 코드를 아래와 같이 개선!
    def solution(people, limit):
    answer = 0
    people.sort()
    idx = 0

    # 한번 움직일 때 최대한 많은 사람 태워서 이동해야함
    for i in range(len(people)-1, -1, -1):
        if people[i] == 0:
            continue
        weight = people[i]
        for j in range(idx, i):
            if weight+people[j] <= limit:
                weight += people[j]
                people[j] = 0
            else:
                idx = j
                break
        answer += 1

    return answer

    """

    # 최종 가장 효율적인 코드
    answer = 0
    people.sort()

    left = 0  # 왼쪽 인덱스
    right = len(people) - 1  # 오른쪽 인덱스

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        answer += 1

    return answer
