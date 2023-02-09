import sys

lst = []
N = int(sys.stdin.readline())
drink = [0]*N

for _ in range(N):
    lst.append(int(sys.stdin.readline()))

if N > 3:
    drink[0] = lst[0]
    drink[1] = lst[1]+drink[0]
    drink[2] = max(lst[0]+lst[2], lst[1]+lst[2], lst[0]+lst[1])
    for i in range(3, N):
        drink[i] = max((drink[i-3]+lst[i-1]+lst[i]),
                       (drink[i-2]+lst[i]), drink[i-1])
    print(drink[N-1])
elif N < 3:
    print(sum(lst))
else:
    print(max(lst[0]+lst[1], lst[1]+lst[2], lst[0]+lst[2]))
