def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])


def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def solution(n, costs):
    # MST, kruskal 이용
    answer = 0
    parent = [i for i in range(n)]

    # cost를 기준으로 오름차순 정렬
    costs.sort(key=lambda x: x[2])

    # 회로가 만들어지지 않으면 add
    for i in range(len(costs)):
        x = costs[i][0]
        y = costs[i][1]
        if find(parent, x) != find(parent, y):
            union(parent, x, y)
            answer += costs[i][2]

    return answer
