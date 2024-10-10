T = int(input())
for t in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    answer = 0
    v = 0

    for i in range(N-1, -1, -1):
        if price[i] > v:
            v = price[i]
        else:
            answer += (v - price[i])

    print(f"#{t+1} {answer}")

"""
시간초과

T = int(input())
for t in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    answer = 0
    cnt = 0
    accumulate = 0

    for i in range(N):
        if i == N-1:
            if (price[i] * cnt - accumulate) < 0:
                break
            else:
                answer += ((price[i] * cnt) - accumulate)
                break

        if (i < N-1):
            if (price[i] >= max(price[i+1:])):
                answer += ((price[i] * cnt) - accumulate)
                cnt = 0
                accumulate = 0
            else:
                cnt += 1
                accumulate += price[i]



    print(f"#{t+1} {answer}")

"""