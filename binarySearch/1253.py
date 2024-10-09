import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
answer = 0

for i in range(N):
    find = lst[:i] + lst[i + 1:]
    left = 0
    right = len(find) - 1

    while left < right:
        if lst[i] == (find[left] + find[right]):
            answer += 1
            break
        elif lst[i] < (find[left] + find[right]):
            right -= 1

        elif lst[i] > (find[left] + find[right]):
            left += 1


print(answer)