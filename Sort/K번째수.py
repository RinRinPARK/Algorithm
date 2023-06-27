def solution(array, commands):
    answer = []

    for ele in commands:
        arr = array[ele[0]-1:ele[1]]
        arr.sort()
        answer.append(arr[ele[2]-1])

    return answer
