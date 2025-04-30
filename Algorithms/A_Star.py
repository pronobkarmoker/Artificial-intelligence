import heapq
import matplotlib.pyplot as plt
import networkx as nx

def a_star(graph, heuristics, start, goal):
   
    pq = [(heuristics[start], 0, start, [start])]
    visited = set()

    while pq:
        f, g, current, path = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path, g  

        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristics.get(neighbor, float('inf'))
                heapq.heappush(pq, (f_new, g_new, neighbor, path + [neighbor]))

    return None, float('inf')  

if __name__ == "__main__":
    
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('D', 5), ('E', 12)],
        'C': [('F', 2)],
        'D': [('G', 3)],
        'E': [('G', 2)],
        'F': [('E', 3)],
        'G': []
    }

    
    heuristics = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 3,
        'E': 1,
        'F': 4,
        'G': 0
    }

    start_node = 'A'
    goal_node = 'G'

    path, cost = a_star(graph, heuristics, start_node, goal_node)

    if path:
        print("A* Path:", " -> ".join(path))
        print("Total Cost:", cost)
    else:
        print("No path found from", start_node, "to", goal_node)



# G = nx.DiGraph()

# # Add graph edges
# for node, neighbors in graph.items():
#     for neighbor, weight in neighbors:
#         G.add_edge(node, neighbor, weight=weight)

# # Path edges
# a_star_edges = list(zip(path[:-1], path[1:]))

# # Layout positions
# pos = nx.spring_layout(G, seed=42)

# # Plot the graph
# plt.figure(figsize=(10, 6))
# nx.draw(G, pos, with_labels=True, node_color='lightgray', node_size=2000, font_size=14)
# nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'), font_size=12)

# # Highlight path
# nx.draw_networkx_edges(G, pos, edgelist=a_star_edges, edge_color='red', width=3)
# nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='lightgreen', node_size=2200)

# # Title
# plt.title(f"A* Path from {start_node} to {goal_node} (Cost: {cost})", fontsize=14)
# plt.axis('off')
# plt.tight_layout()
# plt.show()