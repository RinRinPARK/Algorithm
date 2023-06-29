from itertools import permutations


def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    numbers = list(numbers)
    nums = []

    for i in range(1, len(numbers)+1):
        lst = list(permutations(numbers, i))
        for j in lst:
            nums.append(int("".join(j)))
    nums = list(set(nums))

    for num in nums:
        if is_prime(num):
            answer += 1

    return answer
