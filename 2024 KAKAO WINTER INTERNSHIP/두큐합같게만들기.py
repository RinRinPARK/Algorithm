# LV.2
# Queue
# 각 큐의 원소 합이 같도록 만들려고. 이때 필요한 작업의 최소 횟수
# 한 번의 pop과 한 번의 insert를 합쳐서 작업을 1회 수행한 것으로 간주
from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    tot1 = sum(queue1)
    tot2 = sum(queue2)
    if (tot1 + tot2) % 2 != 0:
        return -1
    while tot1 != tot2:
        if answer >= 300001 * 3:
            answer = -1
            break
        if tot1 > tot2:
            p = queue1.popleft()
            queue2.append(p)
            # tot에 p를 +- 해줘야지, sum(queue1) 이렇게 전체 sum을 다시 계산하면 시간초과남
            tot1 -= p
            tot2 += p
        else:
            p = queue2.popleft()
            queue1.append(p)
            tot1 += p
            tot2 -= p
        answer += 1
    return answer