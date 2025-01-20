from heapq import heappop, heappush

def a_star_search(graph, start_node, target_node, heuristic):
    open_list = []
    heappush(open_list, (0 + heuristic[start_node], start_node))
    came_from = {start_node: None}
    g_score = {start_node: 0}

    while open_list:
        current_f, current_node = heappop(open_list)

        if current_node == target_node:
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            return path, g_score[target_node]

        for neighbor, weight in graph[current_node].items():
            tentative_g_score = g_score[current_node] + weight
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                heappush(open_list, (f_score, neighbor))
                came_from[neighbor] = current_node

    return None, float('inf')

# Get the graph from the user
user_input = input("Enter the graph as adjacency list with weights (e.g., {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'D': 2}, ...}): ")
graph = eval(user_input)

# Get the heuristic values from the user
heuristic_input = input("Enter the heuristic values as a dictionary (e.g., {'A': 3, 'B': 2, 'C': 1, ...}): ")
heuristic = eval(heuristic_input)

# Get the starting node from the user
start_node = input("Enter the starting node: ")

# Get the target node from the user
target_node = input("Enter the target node: ")

# Perform A* Search algorithm
path, cost = a_star_search(graph, start_node, target_node, heuristic)

# Print the shortest path and cost
if path:
    print("Shortest path from", start_node, "to", target_node, ":", path)
    print("Total cost:", cost)
else:
    print("No path found from", start_node, "to", target_node)
