import networkx as nx
import matplotlib.pyplot as plt
import random

# --- Завдання 1: Створення та аналіз графа ---

# 1. Створення графа
G = nx.Graph()

# Додавання вузлів (локацій в AlgoCity)
nodes = ["Central Station", "University", "Market Square", "Airport", "Business Park", "Old Town", "Hospital"]
G.add_nodes_from(nodes)

# Додавання ребер (прямих маршрутів)
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

# Додамо ваги до ребер для Завдання 3
for u, v, weight in edges:
    G.add_edge(u, v, weight=weight)


# 2. Візуалізація графа
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)  # для відтворюваних результатів
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2500, edge_color='gray', font_size=12, font_weight='bold')
# Додавання ваг ребер на візуалізацію
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Транспортна мережа міста AlgoCity")
plt.show()

# 3. Аналіз основних характеристик
print("--- Аналіз графа транспортної мережі AlgoCity ---")
print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
print("\nСтупінь кожної вершини:")
for node, degree in G.degree():
    print(f"  - {node}: {degree}")