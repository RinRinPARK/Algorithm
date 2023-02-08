import sys

lst = []
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if num == 0:
        lst.pop()
    else:
        lst.append(num)

print(sum(lst))
