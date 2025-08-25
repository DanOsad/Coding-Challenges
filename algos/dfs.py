
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

def dfs(graph, node):
    visited = []
    stack = []

    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop(-1)
        for child in reversed(graph[s]):
            if child not in visited:
                visited.append(child)
                stack.append(child)

    return visited

solve = dfs(graph, 'A')
print(solve)
