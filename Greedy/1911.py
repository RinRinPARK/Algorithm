import sys

N, L = map(int, sys.stdin.readline().split())
lst = []
for _ in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))
lst.sort()
count = 0
last = lst[0][0]

for dist in lst:
    start = dist[0]
    end = dist[1]
    if last > start:
        start = last
        if (end-start) % L == 0:
            count += (end-start)//L
            last = end
        else:
            count += ((end-start)//L+1)
            last = start+((end-start)//L+1)*L
    else:
        if (end-start) % L == 0:
            count += (end-start)//L
            last = end
        else:
            count += ((end-start)//L+1)
            last = start+((end-start)//L+1)*L

print(count)
