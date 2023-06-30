from itertools import permutations


def solution(k, dungeons):
    perm = []
    result = []

    visit = list(permutations(dungeons, len(dungeons)))
    for ele in visit:
        perm.append(list(ele))

    for arr in perm:
        count = 0
        p = k
        for i in arr:
            if (i[0] <= p):
                p -= i[1]
                count += 1
        result.append(count)

    return max(result)
