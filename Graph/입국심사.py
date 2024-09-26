# 모든 사람이 심사를 받는데 걸리는 시간을 최소

# n: 입국 심사를 기다리는 사람 수
# times: 각 심사관이 한 명을 심사하는데 걸리는 시간

def solution(n, times):
    answer = float("inf")
    min_val = min(times)
    max_val = max(times) * n
    
    while min_val <= max_val:
        mid = (min_val + max_val) // 2
        cnt = 0
        for time in times:
            cnt += mid // time
            
        if cnt >= n:
            answer = min(answer, mid)
            max_val = mid - 1
        else:
            min_val = mid + 1
    
    return answer