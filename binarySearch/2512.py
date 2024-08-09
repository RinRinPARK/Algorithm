import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
start = 0
end = max(lst)

while start <= end:
    mid = (start + end) // 2
    total = 0

    for l in lst:
        if l >= mid:
            total += mid
        else:
            total += l

    if total <= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)