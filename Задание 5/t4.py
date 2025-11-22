def dfs_spanning_tree(graph, start_node):
    visited = set()
    stack = [start_node]
    spanning_tree_edges = []

    print(f"Начальная вершина: {start_node}")

    stack = [(None, start_node)]

    while stack:
        parent, vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            if parent is not None:
                spanning_tree_edges.append((parent, vertex))

            print(f"Стек: {[v for p, v in stack]}")

            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append((vertex, neighbor))

    return spanning_tree_edges


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

edges = dfs_spanning_tree(graph, "A")
print("\nРебра каркаса (DFS):")
for u, v in edges:
    print(f"{u} -> {v}")
