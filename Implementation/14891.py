import sys


def turn(wheels, wheel, direct):
    # 일단 방향만 정해놓고 나중에 모두 방향 정해지면 한꺼번에 움직이기

    # 방향정하기
    drct1 = 0
    drct2 = 0
    drct3 = 0
    drct4 = 0
    if wheel == 1:
        if direct == 1:
            drct1 = 1
            if wheels[1][2] != wheels[2][6]:
                drct2 = -1
            if drct2 == -1:
                if wheels[2][2] != wheels[3][6]:
                    drct3 = 1
                if drct3 == 1:
                    if wheels[3][2] != wheels[4][6]:
                        drct4 = -1

        else:
            drct1 = -1
            if wheels[1][2] != wheels[2][6]:
                drct2 = 1
            if drct2 == 1:
                if wheels[2][2] != wheels[3][6]:
                    drct3 = -1
                if drct3 == -1:
                    if wheels[3][2] != wheels[4][6]:
                        drct4 = 1

    elif wheel == 2:
        if direct == 1:
            drct2 = 1
            if wheels[1][2] != wheels[2][6]:
                drct1 = -1
            if wheels[2][2] != wheels[3][6]:
                drct3 = -1
                if drct3 == -1:
                    if wheels[3][2] != wheels[4][6]:
                        drct4 = 1
        else:
            drct2 = -1
            if wheels[1][2] != wheels[2][6]:
                drct1 = 1
            if wheels[2][2] != wheels[3][6]:
                drct3 = 1
                if drct3 == 1:
                    if wheels[3][2] != wheels[4][6]:
                        drct4 = -1
    elif wheel == 3:
        if direct == 1:
            drct3 = 1
            if wheels[3][2] != wheels[4][6]:
                drct4 = -1
            if wheels[3][6] != wheels[2][2]:
                drct2 = -1
                if wheels[2][6] != wheels[1][2]:
                    drct1 = 1
        else:
            drct3 = -1
            if wheels[3][2] != wheels[4][6]:
                drct4 = 1
            if wheels[3][6] != wheels[2][2]:
                drct2 = 1
                if wheels[2][6] != wheels[1][2]:
                    drct1 = -1
    else:
        if direct == 1:
            drct4 = 1
            if wheels[4][6] != wheels[3][2]:
                drct3 = -1
                if wheels[3][6] != wheels[2][2]:
                    drct2 = 1
                    if wheels[2][6] != wheels[1][2]:
                        drct1 = -1
        else:
            drct4 = -1
            if wheels[4][6] != wheels[3][2]:
                drct3 = 1
                if wheels[3][6] != wheels[2][2]:
                    drct2 = -1
                    if wheels[2][6] != wheels[1][2]:
                        drct1 = 1

    # 한꺼번에 움직이기
    lst = [0, drct1, drct2, drct3, drct4]

    for i in range(1, 5):
        if lst[i] == 1:
            new = wheels[i][:7]
            new.insert(0, wheels[i][-1])
            wheels[i] = new
        elif lst[i] == -1:
            new = wheels[i][1:]
            new.insert(7, wheels[i][0])
            wheels[i] = new


wheels = [[] for _ in range(5)]

for i in range(1, 5):
    lst = list(sys.stdin.readline().rstrip())
    for j in lst:
        wheels[i].append(int(j))
K = int(sys.stdin.readline())

for _ in range(K):
    # 리스트에 저장하지 말고 동작 들어올 때마다 바로 수행
    wheel, direct = map(int, sys.stdin.readline().split())
    turn(wheels, wheel, direct)

# 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
# 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
# 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
# 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
ans = 0
for k in range(1, 5):
    if wheels[k][0] == 1:
        ans += 2**(k-1)

print(ans)
