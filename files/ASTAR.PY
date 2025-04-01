import heapq

nodes = {'S': 0, 'B': 12, 'C': 11, 'D': 6, 'E': 4, 'K': 4, 'G': 0}

path_weights = {
    'S': {'B': 4, 'C': 3},
    'B': {'K': 5, 'E': 12},
    'C': {'E': 10, 'D': 7},
    'D': {'E': 2},
    'E': {'G': 5},
    'K': {'G': 16},
    'G': {}
}

def astar(graph, heuristics, start, goal):
    open_list = [(heuristics[start], 0, start, [])]
    heapq.heapify(open_list)
    
    while open_list:
        _, cost, node, path = heapq.heappop(open_list)
        path = path + [node]
        
        if node == goal:
            return path, cost
        
        for neighbor, weight in graph[node].items():
            heapq.heappush(open_list, (cost + weight + heuristics[neighbor], cost + weight, neighbor, path))
    
    return None, float('inf')

start, goal = 'S', 'G'
path, cost = astar(path_weights, nodes, start, goal)

if path:
    print("Shortest Path:", " → ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found.")
