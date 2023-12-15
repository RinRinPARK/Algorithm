import sys
from collections import deque

N=int(sys.stdin.readline())
cards = deque([i for i in range(1, N+1)])

while (len(cards) > 1):
    cards.popleft()
    num = cards.popleft()
    cards.append(num)

print(cards[0])