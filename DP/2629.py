import sys

S = int(sys.stdin.readline())
S_weight = list(map(int, sys.stdin.readline().split()))
B = int(sys.stdin.readline())
B_weight = list(map(int, sys.stdin.readline().split()))

# 추의 무게들을 더하고 빼서 구슬의 무게를 만들 수 있나 확인
dp = [0]
for sinker in S_weight:
    lst = []
    for d in dp:
        lst.append(d + sinker)
        lst.append(abs(d - sinker))
    dp = list(set(dp + lst))

for bead in B_weight:
    if bead in dp:
        print("Y", end = ' ')
    else:
        print("N", end = ' ')        
