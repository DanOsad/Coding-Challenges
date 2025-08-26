
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
    stack = [] # FILO

    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop(-1)
        for child in reversed(graph[s]):
            if child not in visited:
                visited.append(child)
                stack.append(child)

    return visited

def dfs_recursive(graph, node):
    visited = []

    def traverse(node):
        if not node:
            return
        traverse(node.left)
        visited.append(node)
        traverse(node.right)

    return visited

solve = dfs(graph, 'A')
print(solve)
