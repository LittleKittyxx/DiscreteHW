import heapq


def prim_mst(graph, start_node):
    mst = []
    visited = set()
    min_heap = []

    visited.add(start_node)

    for neighbor, weight in graph[start_node]:
        heapq.heappush(min_heap, (weight, start_node, neighbor))

    while min_heap:
        weight, u, v = heapq.heappop(min_heap)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))

            for next_node, next_weight in graph[v]:
                if next_node not in visited:
                    heapq.heappush(min_heap, (next_weight, v, next_node))

    return mst


my_graph = {
    "A": [("B", 2), ("C", 3)],
    "B": [("A", 2), ("C", 1), ("D", 1)],
    "C": [("A", 3), ("B", 1), ("D", 4)],
    "D": [("B", 1), ("C", 4)],
}

result_mst = prim_mst(my_graph, "A")
print("Ребра каркаса (откуда, куда, вес):")
for edge in result_mst:
    print(edge)


"""

Ребра каркаса (откуда, куда, вес):
('A', 'B', 2)
('B', 'C', 1)
('B', 'D', 1)

"""
