import sys

N = int(sys.stdin.readline())

num = 0
count = 0
while 1:
    if '666' in str(num):
        count += 1
        if count == N:
            print(num)
            break
    num += 1
