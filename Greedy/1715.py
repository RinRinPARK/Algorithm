import heapq
import sys

N = int(sys.stdin.readline())
card = []
count = 0

for _ in range(N):
    heapq.heappush(card, int(sys.stdin.readline()))

if len(card) == 1:
    print(0)
else:
    while len(card) > 1:
        stage = heapq.heappop(card)+heapq.heappop(card)
        count = count+stage
        heapq.heappush(card, stage)
    print(count)
