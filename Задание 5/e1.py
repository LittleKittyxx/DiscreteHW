import networkx as nx
import matplotlib.pyplot as plt
import collections
import time


def visualize_algo(graph_dict, start_node, algo="bfs"):
    G = nx.Graph(graph_dict)
    pos = nx.spring_layout(G, seed=42)

    colors = {node: "lightgray" for node in G.nodes()}

    plt.ion()
    fig, ax = plt.subplots(figsize=(8, 6))

    def draw_step(active_node=None, queue_stack=None):
        ax.clear()
        ax.set_title(
            f"Алгоритм: {algo.upper()} | Активен: {active_node} | Структура: {list(queue_stack) if queue_stack else []}"
        )

        node_colors_list = []
        for node in G.nodes():
            if node == active_node:
                node_colors_list.append("red")
            elif queue_stack and node in queue_stack:
                node_colors_list.append("yellow")
            elif colors[node] == "visited":
                node_colors_list.append("lightgreen")
            else:
                node_colors_list.append("lightgray")

        nx.draw(
            G,
            pos,
            ax=ax,
            with_labels=True,
            node_color=node_colors_list,
            node_size=800,
            font_weight="bold",
            edge_color="gray",
        )
        plt.draw()
        plt.pause(1.0)

    if algo == "bfs":
        visited = set([start_node])
        colors[start_node] = "visited"
        queue = collections.deque([start_node])

        while queue:
            draw_step(active_node=None, queue_stack=queue)
            curr = queue.popleft()

            draw_step(active_node=curr, queue_stack=queue)

            for neighbor in graph_dict[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    colors[neighbor] = "visited"
                    queue.append(neighbor)
                    draw_step(active_node=curr, queue_stack=queue)

    elif algo == "dfs":
        visited = set()
        stack = [start_node]

        while stack:
            draw_step(active_node=None, queue_stack=stack)
            curr = stack.pop()

            if curr not in visited:
                visited.add(curr)
                colors[curr] = "visited"
                draw_step(active_node=curr, queue_stack=stack)

                for neighbor in reversed(graph_dict[curr]):
                    if neighbor not in visited:
                        stack.append(neighbor)
                        draw_step(active_node=curr, queue_stack=stack)

    ax.clear()
    ax.set_title(f"{algo.upper()} Завершен")
    nx.draw(G, pos, ax=ax, with_labels=True, node_color="lightgreen", node_size=800)
    plt.ioff()
    plt.show()


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print("1. Визуализация BFS")
print("2. Визуализация DFS")
choice = input("Выберите (1 или 2): ")

if choice == "1":
    visualize_algo(graph, "A", "bfs")
else:
    visualize_algo(graph, "A", "dfs")
