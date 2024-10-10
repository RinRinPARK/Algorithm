import math

T = int(input())
cases = []


for _ in range(T):
    cases.append(list(map(int, input().split())))

t = 1
for case in cases:
    ans = 0

    for num in case:
        if (num % 2) != 0:
            ans += num

    print("#", t, " ", ans, sep = "")
    t += 1