import sys

N = int(sys.stdin.readline())
stairs = [0]*301
for j in range(N):
    stairs[j] = int(sys.stdin.readline())
scores = [0]*301

scores[0] = stairs[0]
scores[1] = max(stairs[0]+stairs[1], stairs[1])
scores[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])

for i in range(3, N):
    scores[i] = (max(scores[i-2]+stairs[i], scores[i-3]+stairs[i-1]+stairs[i]))

print(scores[N-1])
