import collections


def bfs(graph, start_node):
    visited = set()
    queue = collections.deque([start_node])
    visited.add(start_node)

    print(f"Начальная вершина: {start_node}")

    while queue:
        print(f"Текущая очередь: {list(queue)}")

        vertex = queue.popleft()
        print(f"Обработка вершины: {vertex}")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print("Обход завершен.\n")


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

bfs(graph, "A")
