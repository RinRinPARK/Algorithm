# 당신이 모은 양의 수보다 늑대의 수가 같거나 더 많아지면 바로 모든 양을 잡아먹어 버립니다.
# info: 양 또는 늑대에 대한 정보가 담긴 배열
# edges: 2진 트리의 각 노드들의 연결 관계를 담은 2차원 배열


# 갈 수 있는 곳을 다 방문하면 끝나는걸로
# 중간 중간 양 갯수 확인하면서 max 값 변경

answer = 0
roads = []
infoes = []

def dfs(x, visited, cnt, sheep, wolf):
    global answer, roads, infoes
    
    if infoes[x] == 0:
        sheep += 1
        cnt += 1
        answer = max(answer, cnt)
    elif infoes[x] == 1:
        wolf += 1
        if sheep <= wolf:
            return
        
    for node in visited:
        for next in roads[node]:
            if next not in visited:
                visited.append(next)
                dfs(next, visited, cnt, sheep, wolf)
                visited.pop()
    
    return


def solution(info, edges):
    global answer, roads, infoes
    
    infoes = info
    
    roads = [[] for _ in range(len(info))]
    
    for a, b in edges:
        roads[a].append(b)
        
    dfs(0, [0], 0, 0, 0)
        
    return answer