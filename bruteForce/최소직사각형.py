def solution(sizes):
    answer = 0
    width = 0
    height = 0

    for arr in sizes:
        arr.sort()
        if width < arr[0]:
            width = arr[0]
        if height < arr[1]:
            height = arr[1]

    answer = width * height

    return answer
