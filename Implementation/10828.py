import sys
from collections import deque

def stack(cmd, queue):
    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(queue) == 0:
            print(-1)
        else:
            num = queue.pop()
            print(num)
            queue.append(num)


N = int(sys.stdin.readline())
queue = deque()
for _ in range(N):
    cmd = list(map(str, sys.stdin.readline().split()))
    stack(cmd, queue)
