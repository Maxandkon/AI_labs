import matplotlib.pyplot as plt
from collections import deque
import networkx as nx 
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A','D'],
    'D': ['C', 'F','A', 'G'],
    'E': ['B', 'H'],
    'F': ['D', 'H'],
    'G': ['D', 'H', 'J'],
    'H': ['E', 'G', 'I', 'F'],
    'I': ['H', 'K', 'J'],
    'J': ['G', 'I', 'KK'],
    'K': ['I', 'KK'],
    'KK': ['K', 'J']
}


start_node = 'C'
end_node = 'KK'


def breadth_first_search(graph, start, end):
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path

        if current not in graph:
            continue

        for neighbor in graph[current]:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))

    return None


optimal_route_bfs = breadth_first_search(graph, start_node, end_node)

if optimal_route_bfs:
    print(f"Оптимальний маршрут від {start_node} до {end_node}: {optimal_route_bfs}")
else:
    print(f"Маршрут від {start_node} до {end_node} не знайдено.")


def plot_graph(graph, optimal_route):
    plt.figure(figsize=(8, 6))
    pos = {
        'A': (0, 0),
        'B': (1, 0),
        'C': (0, 1),
        'D': (1, 1),
        'E': (2, 0),
        'F': (2, 1),
        'G': (3, 0),
        'H': (3, 1),
        'I': (4, 1),
        'J': (4, 0),
        'K': (5, 1),
        'KK': (6, 1)
    }

    nx_graph = {node: [] for node in graph}
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            nx_graph[node].append(neighbor)

    nx.draw(nx.Graph(nx_graph), pos, with_labels=True, node_size=500, node_color='lightblue')
    if optimal_route:
        edges = [(optimal_route[i], optimal_route[i + 1]) for i in range(len(optimal_route) - 1)]
        nx.draw_networkx_edges(nx.Graph(nx_graph), pos, edgelist=edges, edge_color='red', width=2)
    plt.show()


plot_graph(graph, optimal_route_bfs)
