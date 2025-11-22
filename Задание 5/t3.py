import collections


def bfs_spanning_tree(graph, start_node):
    visited = set()
    queue = collections.deque([start_node])
    visited.add(start_node)
    spanning_tree_edges = []

    print(f"Начальная вершина: {start_node}")

    while queue:
        print(f"Очередь: {list(queue)}")
        vertex = queue.popleft()

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                spanning_tree_edges.append((vertex, neighbor))

    return spanning_tree_edges


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

edges = bfs_spanning_tree(graph, "A")
print("\nРебра каркаса (BFS):")
for u, v in edges:
    print(f"{u} -> {v}")
