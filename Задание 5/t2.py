def dfs(graph, start_node):
    visited = set()
    stack = [start_node]

    print(f"Начинаем обход в глубину с вершины: {start_node}")

    while stack:
        print(f"Текущий стек: {stack}")

        vertex = stack.pop()

        if vertex not in visited:
            print(f"Обработка вершины: {vertex}")
            visited.add(vertex)

            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)

    print("Обход завершен.\n")


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

dfs(graph, "A")
