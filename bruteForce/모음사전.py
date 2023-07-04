from itertools import product


def solution(word):

    alpha = ['A', 'E', 'I', 'O', 'U']
    dict = []

    for i in range(1, 6):
        lst = list(product(alpha, repeat=i))
        for arr in lst:
            dict.append("".join(arr))
    dict.sort()

    answer = dict.index(word)+1

    return answer
