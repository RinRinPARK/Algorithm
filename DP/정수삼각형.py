def solution(triangle):
    answer = 0
    
    dp = [[0 for _ in range(len(triangle[-1]))] for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    
    if len(triangle) == 1:
        return dp[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            dp[i][j] = max(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])
            answer = max(answer, dp[i][j])
            
            
    return answer