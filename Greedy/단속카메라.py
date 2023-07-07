def solution(routes):
    answer = 0

    routes.sort(key=lambda x: x[1])

    loc = routes[0][1]

    for route in routes:
        if loc < route[0]:
            answer += 1
            loc = route[1]

    return answer+1
