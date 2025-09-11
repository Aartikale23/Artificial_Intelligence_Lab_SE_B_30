from queue import PriorityQueue

# Example graph
graph = {
    'S': {'A': 3, 'B': 1, 'C':8},
    'A': {'D': 3, 'E': 7, 'G': 15},
    'B': {'G': 20},
    'C': {'G': 5},
    'D': {},
    'E': {},
    'G': {}
}

# Heuristic values
heuristics = {
    'S': 20, 'A': 12, 'B': 17,
    'C': 25, 'D': 17, 'E': 10, 'G':0
}

def a_star_search(start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))
    g_cost = {start: 0}
    parent = {start: None}

    while not open_list.empty():
        f, current = open_list.get()

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1], g_cost[goal]

        for neighbor, cost in graph[current].items():
            tentative_g = g_cost[current] + cost
            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + heuristics[neighbor]
                open_list.put((f_cost, neighbor))
                parent[neighbor] = current

    return None, float("inf")

# Run A*
start, goal = 'S', 'G'
path, cost = a_star_search(start, goal)
print("Optimal Path:", path)
print("Total Cost:", cost)

