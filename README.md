# Day-20-A-Search-Algorithm-
Here Python Program for A* Search Algorithm. Day 20 of Day 365.
- Concept: A* Search Algorithm is a popular pathfinding and graph traversal algorithm used to find the shortest path between nodes in a graph. It combines the strengths of Dijkstra's Algorithm and Greedy Best-First Search.

- Key Components:
    1. Graph: A network of nodes (vertices) connected by edges.
    2. Start Node: The node where the search begins.
    3. Goal Node: The target node the algorithm aims to reach.
    4. g(n): The cost of the path from the start node to the current node n.
    5. h(n): The heuristic function that estimates the cost from the current node n to the goal node.
    6. f(n): The total estimated cost of the cheapest solution through the current node n. It's calculated as f(n) = g(n) + h(n).

- Steps:
    1. Initialize:
        - Add the start node to an open list (nodes to be evaluated).
        - Set g(start) = 0 and h(start) = heuristic estimate to the goal.
    2. Loop:
        - While the open list is not empty:
            - Choose the node with the lowest f(n) from the open list.
            - If this node is the goal node, the path is found and the algorithm terminates.
            - Move this node to the closed list (nodes already evaluated).
            - For each neighbor of the current node:
                - Calculate the tentative g score (g(current) + cost to move to the neighbor).
                - If the neighbor is not in the open list, add it with the calculated f score.
                - If the neighbor is in the open list but the new g score is lower, update the neighbor's score.
    3. Path Construction:
        - Once the goal node is reached, backtrack from the goal node to the start node to reconstruct the path.

- Characteristics:
    - Optimality: A* is optimal if the heuristic function h(n) is admissible (never overestimates the cost to reach the goal).
    - Completeness: A* is complete, meaning it will always find a solution if one exists.
    - Efficiency: A* is more efficient than other algorithms like Dijkstra's because it uses heuristics to guide the search.

Here's a simple visual example:
```
Start -> A -> B -> Goal
```
In this example, A* uses the heuristic to prioritize nodes closer to the goal and finds the shortest path efficiently.
