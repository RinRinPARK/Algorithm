from collections import deque

def solution(n, edge):
    
    dict = {}
    
    for a, b in edge:
        if a in dict.keys():
            dict[a].append(b)
        else:
            dict[a] = [b]
            
        if b in dict.keys():
            dict[b].append(a)
        else:
            dict[b] = [a]
    
    visited = [float("inf") for _ in range(n + 1)]
    
    queue = deque()
    queue.append([1, 0])
    
    while queue:
        x, v = queue.popleft()
        
        for n in dict[x]:
            if visited[n] > v + 1:
                visited[n] = v + 1
                queue.append([n, v + 1])
                
    value = max(visited[2:])
        
    return visited[2:].count(value)