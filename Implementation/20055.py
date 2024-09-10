import sys

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
robots = [0 for _ in range(N * 2)]
cnt = 0  # 내구도가 0인 칸의 개수를 추적하는 변수
ans = 0
head = 0

# 내구도가 0인 칸의 초기 개수를 카운트
for durability in A:
    if durability == 0:
        cnt += 1

while cnt < K:
    ans += 1

    # 1. 벨트가 한 칸 회전
    head = (head + (2 * N - 1)) % (2 * N)

    # 내리는 위치(N번째 칸)에서 로봇을 내림
    if robots[(head + (N - 1)) % (2 * N)] == 1:
        robots[(head + (N - 1)) % (2 * N)] = 0

    # 2. 로봇 이동 처리 (가장 먼저 올라간 로봇부터 처리)
    for i in range(N - 2, -1, -1):
        pt = (head + i) % (2 * N)
        nxt = (pt + 1) % (2 * N)

        if robots[pt] == 1 and robots[nxt] == 0 and A[nxt] > 0:
            # 로봇을 다음 칸으로 이동
            robots[pt] = 0
            robots[nxt] = 1
            A[nxt] -= 1

            # 내구도가 0이 되었으면 cnt 증가
            if A[nxt] == 0:
                cnt += 1

    # 내리는 위치(N번째 칸)에서 로봇을 내림
    robots[(head + (N - 1)) % (2 * N)] = 0

    # 3. 올리는 위치에 로봇을 올림
    if A[head] > 0:
        robots[head] = 1
        A[head] -= 1

        # 내구도가 0이 되었으면 cnt 증가
        if A[head] == 0:
            cnt += 1

print(ans)