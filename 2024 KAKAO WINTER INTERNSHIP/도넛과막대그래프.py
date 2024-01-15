def solution(edges):
    # 도넛: 모든 정점이 in - 1, out - 1
    # 막대: 마지막 정점이 in - 1, out - 0 (만약 생성 정점이 연결된 경우 in >= 1)
    # 8자: 중간 정점이 in - 2, out - 2(만약 생성 정점이 연결된 경우 in >= 2)
    # 생성정점: in - 0, out - n
    n = 0
    created = 0
    donut = 0
    stick = 0
    eight = 0
    in_arr = [0 for _ in range(1000001)]
    out_arr = [0 for _ in range(1000001)]
    for a, b in edges:
        n = max(n, a, b)
        in_arr[b] += 1
        out_arr[a] += 1
    for k in range(1, n+1):
        if in_arr[k] == 0 and out_arr[k] > 1:
            created = k
        elif in_arr[k] >= 1 and out_arr[k] == 0:
            stick += 1
        elif in_arr[k] >= 2 and out_arr[k] == 2:
            eight += 1
    donut = out_arr[created] - (stick + eight) 
    answer = [created, donut, stick, eight]
    return answer