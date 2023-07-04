def solution(n, lost, reserve):
    nlost = set(lost) - set(reserve)
    nreserve = set(reserve) - set(lost)

    for i in nreserve:
        if (i-1 in nlost):
            nlost.remove(i-1)
        elif (i+1 in nlost):
            nlost.remove(i+1)

    return n-len(nlost)
