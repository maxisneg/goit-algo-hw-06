import networkx as nx
import matplotlib.pyplot as plt
import heapq


G = nx.Graph()

nodes = ["Central Station", "University", "Market Square", "Airport", "Business Park", "Old Town", "Hospital"]
G.add_nodes_from(nodes)

edges = [
    ("Central Station", "University", 1),
    ("Central Station", "Market Square", 2),
    ("Central Station", "Airport", 5),
    ("University", "Business Park", 2),
    ("Market Square", "Old Town", 1),
    ("Market Square", "Hospital", 3),
    ("Business Park", "Airport", 3),
    ("Old Town", "Hospital", 1)
]

for u, v, w in edges:
    G.add_edge(u, v, weight=w)

#  Візуалізація графа 
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2500, edge_color='gray', font_size=12)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Транспортна мережа AlgoCity")
plt.show()


def dijkstra_all(graph, start):
    """Знаходить найкоротші шляхи від start до всіх інших вершин."""
    queue = [(0, start, [])]
    visited = set()
    min_costs = {start: 0}
    paths = {start: [start]}

    while queue:
        (cost, vertex, path) = heapq.heappop(queue)
        if vertex in visited:
            continue
        visited.add(vertex)
        path = path + [vertex]

        for neighbor in graph[vertex]:
            total_cost = cost + graph[vertex][neighbor]['weight']
            if neighbor not in min_costs or total_cost < min_costs[neighbor]:
                min_costs[neighbor] = total_cost
                paths[neighbor] = path + [neighbor]
                heapq.heappush(queue, (total_cost, neighbor, path))

    return min_costs, paths

# Вивід результатів для всіх вершин 
print("\n--- Завдння 3: Найкоротші шляхи між усіма вершинами (алгоритм Дейкстри) ---")
for node in G.nodes():
    costs, paths = dijkstra_all(G, node)
    print(f"\nВід '{node}':")
    for target in G.nodes():
        if target == node:
            continue
        print(f"  → {target}: Шлях = {paths.get(target, 'недоступно')}, Вага = {costs.get(target, '∞')}")
