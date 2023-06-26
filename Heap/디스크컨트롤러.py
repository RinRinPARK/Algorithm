import heapq


def solution(jobs):
    answer = 0
    heap = []
    count, start, finish = 0, -1, 0

    while count < len(jobs):
        for j in jobs:
            if start < j[0] <= finish:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            ele = heapq.heappop(heap)
            start = finish
            finish += ele[0]
            answer += (finish - ele[1])
            count += 1
        else:
            finish += 1

    return answer//len(jobs)
