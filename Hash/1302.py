import sys

N = int(sys.stdin.readline())
dict = {}

for _ in range(N):
    book = sys.stdin.readline().strip()
    if book in dict:
        dict[book] += 1
    else:
        dict[book] = 1

result = ''
check = 0
for key in dict.keys():
    if dict[key] > check:
        result = key
        check = dict[key]
    elif dict[key] == check:
        result = min(result, key)

print(result)