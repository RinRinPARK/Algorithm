import sys
import heapq

leftHeap = []
rightHeap = []
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)
    if rightHeap and -leftHeap[0] > rightHeap[0]:
        a = -heapq.heappop(leftHeap)
        b = heapq.heappop(rightHeap)
        heapq.heappush(leftHeap, -b)
        heapq.heappush(rightHeap, a)
    print(-leftHeap[0])
