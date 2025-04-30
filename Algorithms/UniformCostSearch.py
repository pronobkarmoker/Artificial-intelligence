import heapq

def uniform_cost_search(graph, start, goal):
   
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, current, path = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path, cost

        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))

    return None, float('inf')  


if __name__ == "__main__":
    # Define the graph as an adjacency list
    graph = {
        'A': [('B', 2), ('C', 5)],
        'B': [('D', 4), ('E', 7)],
        'C': [('F', 2)],
        'D': [('G', 1)],
        'E': [('G', 3)],
        'F': [('E', 1)],
        'G': []
    }

    start_node = 'A'
    goal_node = 'G'

    path, total_cost = uniform_cost_search(graph, start_node, goal_node)

    if path:
        print("Path found:")
        print(" -> ".join(path))
        print("Total Cost:", total_cost)
    else:
        print("No path found from", start_node, "to", goal_node)
