import matplotlib.pyplot as plt
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'F'],
    'D': ['A', 'G'],
    'E': ['B', 'H'],
    'F': ['C', 'I'],
    'G': ['D', 'H', 'J'],
    'H': ['E', 'G', 'K'],
    'I': ['F'],
    'J': ['G'],
    'K': ['H']
}
def depth_first_search(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = depth_first_search(graph, neighbor, end, path)
            if new_path:
                return new_path
    return None

start_node = 'A'
end_node = 'K'
#aicfahaedj
optimal_route = depth_first_search(graph, start_node, end_node)

if optimal_route:
    print(f"Оптимальний маршрут від {start_node} до {end_node}: {optimal_route}")
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
        'K': (5, 1)
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

plot_graph(graph, optimal_route)
