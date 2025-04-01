class Node:
    def __init__(self, name, heuristics):
        self.name = name
        self.heuristics = heuristics
        self.children = []
        self.cost = float('inf')
    def add_child(self, child, cost):
        self.children.append((child, cost))

def aostar_search(node):
    if not node.children:
        node.cost = node.heuristics
        return node.cost
    min_cost = float('inf')
    for child, cost in node.children:
        child_cost = aostar_search(child) + cost
        if child_cost < min_cost:
            min_cost = child_cost
    
    node.cost = min_cost 
    return node.cost

S = Node('S',5)
A = Node('A',2)
B = Node('B',3)
C = Node('C',1)
D = Node('D',4)
E= Node('E',0)
F = Node('F',0)

S.add_child(A, 1)
S.add_child(B, 2)
A.add_child(C, 1)
A.add_child(D, 3)
B.add_child(E, 5)
D.add_child(F, 2)

aostar_search(S)
print("Minimum cost:", S.cost)