import heapq


def solution(operations):
    answer = []
    heap = []

    for opr in operations:
        opr = opr.split(" ")
        if opr[0] == "I":
            heapq.heappush(heap, int(opr[1]))
        else:
            if (opr[1] == "1") and (len(heap) > 0):
                heap.pop(heap.index(max(heap)))
            elif (opr[1] == "-1") and (len(heap) > 0):
                heapq.heappop(heap)

    if len(heap) > 0:
        answer = [int(heap[heap.index(max(heap))]), int(heap[0])]
    else:
        answer = [0, 0]

    return answer
