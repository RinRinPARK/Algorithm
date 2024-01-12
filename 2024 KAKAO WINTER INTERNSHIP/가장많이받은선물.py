# Lv.1
def solution(friends, gifts):
    # 선물지수 = 준 선물 - 받은 선물
    # 선물지수가 큰 사람이 작은 사람에게 받음
    # 다음달에 가장 많은 선물을 받을 친구의 선물의 수 return
    N = len(friends)
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    next = [0 for _ in range(N)]
    factors = [0 for _ in range(N)] # 선물지수
    
    for gift in gifts:
        A, B = map(str, gift.split())
        idxG = friends.index(A)
        idxT = friends.index(B)
        matrix[idxG][idxT] += 1
        factors[idxG] += 1
        factors[idxT] -= 1
    
    for i in range(N):
        for j in range(i+1, N):
            if matrix[i][j] == matrix[j][i]:
                if factors[i] == factors[j]:
                    continue
                if factors[i] > factors[j]:
                    next[i] += 1
                elif factors[j] > factors[i]:
                    next[j] += 1
            elif matrix[i][j] < matrix[j][i]:
                next[j] += 1
            elif matrix[i][j] > matrix[j][i]:
                next[i] += 1
    answer = max(next)
    return answer