def solution(priorities, location):
    answer = 0
    count = 0

    while answer == 0:
        for i in range(len(priorities)):
            if priorities[i] >= max(priorities):
                if i == location:
                    count += 1
                    answer = count
                    break
                else:
                    count += 1
                    priorities[i] = 0

    return answer
