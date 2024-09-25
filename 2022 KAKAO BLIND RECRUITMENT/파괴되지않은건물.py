# board: 건물의 내구도를 나타내는 2차원 정수 배열
# skill: 적의 공격 혹은 아군의 회복 스킬([type, r1, c1, r2, c2, degree])

# 적의 공격 혹은 아군의 회복 스킬이 모두 끝난 뒤 파괴되지 않은 건물의 개수를 return
def solution(board, skill):
    answer = 0
    tmp = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        tmp[r1][c1] += degree if type==2 else (-1)*degree
        tmp[r1][c2+1] += degree if type==1 else (-1)*degree
        tmp[r2+1][c1] += degree if type==1 else (-1)*degree
        tmp[r2+1][c2+1] += degree if type==2 else (-1)*degree
        
    for i in range(len(board)):
        for j in range(len(board[0]) - 1):
            tmp[i][j+1] += tmp[i][j]

            
    for i in range(len(board) - 1):
        for j in range(len(board[0])):
            tmp[i+1][j] += tmp[i][j]
            
    for x in range(len(board)):
        for y in range(len(board[0])):
            board[x][y] += tmp[x][y]
            if board[x][y] > 0:
                answer+=1
                
    return answer