import sys

# 가로수들이 모두 같은 간격이 되도록 가로수를 추가로 심는 사업을 추진

# 유클리드 호제법
def gcd(a,b):
    while b > 0:
        a,b = b,a % b
    return a

n = int(sys.stdin.readline())
trees = []

for _ in range(n):
    trees.append(int(sys.stdin.readline()))

# 사이 간격의 최대공약수 구한 후 그 간격만큼 필요한 가로수 개수 구하기
interval = []
for i in range(n-1):
    interval.append(trees[i+1] - trees[i])

interval.sort()
a = interval[0]
for j in range(len(interval)):
    a = gcd(a, interval[j])

result = 0
for b in interval:
    result += ((b // a)-1)

print(result)