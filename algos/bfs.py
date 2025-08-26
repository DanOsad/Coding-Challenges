
graph = {
    'A': ['B','G'],
    'B': ['C','D','E'],
    'C': [],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': ['H'],
    'H': ['I'],
    'I': []
}

def bfs(graph, node):
    visited = []
    queue = [] # FIFO

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
    
    return visited

solve = bfs(graph, 'A')

print(solve)