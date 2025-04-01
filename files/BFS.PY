def bfs(adj):
    V = len(adj)
    res = []
    start = 0
    from collections import deque
    queue = deque([start])
    visited = [False] * V
    visited[start] = True
    
    while queue:
        current = queue.popleft()
        res.append(current)
        
        for neighbor in adj[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                
    return res


adj = [[1,2], [0,2,3], [0,4], [1,4], [2,3]]
ans = bfs(adj)
for i in ans:
    print(i, end=" ")