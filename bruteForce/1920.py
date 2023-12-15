import sys

N = int(sys.stdin.readline())
dict = list(map(int,sys.stdin.readline().split()))
dict.sort()
M = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

for num in nums:
    left = 0
    right = N-1
    flag = 0
    while left <= right:
        mid = (left + right)//2

        if (dict[mid] == num):
            print(1)
            flag = 1
            break

        elif (dict[mid] < num):
            left = mid + 1

        elif (dict[mid] > num):
            right = mid -1

    if flag == 0:
        print(0)
