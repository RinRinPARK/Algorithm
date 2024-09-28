import sys

# 색종이의 크기는 1×1, 2×2, 3×3, 4×4, 5×5로 총 다섯 종류가 있으며, 각 종류의 색종이는 5개씩
# 1이 적힌 칸은 모두 색종이로 덮여져야 한다. 
# 색종이를 붙일 때는 종이의 경계 밖으로 나가서는 안되고, 겹쳐도 안 된다. 
# 또, 칸의 경계와 일치하게 붙여야 한다. 0이 적힌 칸에는 색종이가 있으면 안 된다.

# 1이 적힌 모든 칸을 붙이는데 필요한 색종이의 최소 개수
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
papers = [5, 5, 5, 5, 5]
answer = float("inf")
visited = [[0 for _ in range(1)] for _ in range(10)]

def dfs():
    global answer

    # 다 덮었는지 확인
    f = 0
    for a in range(10):
        for b in range(10):
            if graph[a][b] == 1:
                f = 1
                break
        if f == 1:
            break
    if f == 0:
        answer = min(answer, 25 - sum(papers))
        return
    
    # 색종이 붙이기 시작
    for i in range(10):
        for j in range(10):
            if graph[i][j] == 1:
                for k in range(1, 6):
                    # 붙일 수 있는지 확인
                    if papers[k-1] > 0:
                        flag = 0
                        for m in range(i, i+k):
                            for n in range(j, j+k):
                                if not((0 <= m < 10) and (0 <= n < 10)):
                                    flag = 1
                                    break
                                else:
                                    if graph[m][n] != 1:
                                        flag = 1
                                        break
                            if flag == 1:
                                break

                        # 붙이기
                        if flag == 0:
                            for m in range(i, i+k):
                                for n in range(j, j+k):
                                        graph[m][n] = 0
                            
                            papers[k-1] -= 1
                            dfs()
                            papers[k-1] += 1
                            for m in range(i, i+k):
                                for n in range(j, j+k):
                                        graph[m][n] = 1
                                        
                return

dfs()

print(answer if answer != float("inf") else -1)