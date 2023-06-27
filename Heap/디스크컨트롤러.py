import heapq


def solution(jobs):
    answer = 0
    count = 0  # 모든 작업을 마쳤는지 확인
    start = -1  # 이전 작업이 시작한 시점
    finish = 0  # 이전 작업이 끝난 시점
    heap = []

    while count < len(jobs):
        for ele in jobs:
            if start < ele[0] <= finish:
                heapq.heappush(heap, [ele[1], ele[0]])
        if len(heap) > 0:
            arr = heapq.heappop(heap)
            count += 1
            start = finish
            finish = finish + arr[0]
            answer += (finish-arr[1])
        else:
            finish += 1

    return answer//len(jobs)
