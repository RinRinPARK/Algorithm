# bfs 아이디어
def solution(n, wires):
    answer = float("inf")

    # wires에서 순서대로 하나씩 끊으면서 값을 비교한다.
    for i in range(len(wires)):
        graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
        visited = [0] * (n+1)
        queue = []

        for arr in wires:
            if arr == wires[i]:
                continue
            x = arr[0]
            y = arr[1]
            graph[x][y] = 1
            graph[y][x] = 1

        idx = (i+1) % len(wires)
        queue.append(wires[idx][0])
        queue.append(wires[idx][1])

        while queue:
            x = queue.pop(0)
            if visited[x] == 0:
                visited[x] = 1
                for j in range(len(graph[x])):
                    if (graph[x][j] == 1) and (visited[j] == 0):
                        queue.append(j)

        answer = min(answer, abs(visited.count(1) - (visited.count(0)-1)))
    return answer
