def solution(nums):
    answer = 0
    dict = {}
    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 0
    if len(nums)//2 > len(dict):
        answer = len(dict)
    else:
        answer = len(nums)
    return answer
