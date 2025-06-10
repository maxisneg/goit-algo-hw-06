from collections import deque

# --- Завдання 2: Реалізація DFS та BFS ---

def dfs_path(graph, start, goal):
    """Знаходить шлях за допомогою DFS."""
    stack = [(start, [start])]
    visited = {start}
    while stack:
        (vertex, path) = stack.pop()
        for neighbor in graph[vertex]:
            if neighbor == goal:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))
    return None

def bfs_path(graph, start, goal):
    """Знаходить шлях за допомогою BFS."""
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        (vertex, path) = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor == goal:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

# Знаходження шляхів між 'University' та 'Hospital'
start_node = 'University'
end_node = 'Hospital'

path_dfs = dfs_path(G, start_node, end_node)
path_bfs = bfs_path(G, start_node, end_node)

print(f"\n--- Пошук шляхів від '{start_node}' до '{end_node}' ---")
print(f"Шлях, знайдений DFS: {path_dfs}")
print(f"Шлях, знайдений BFS: {path_bfs}")