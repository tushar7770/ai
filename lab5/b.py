import heapq

def tsp_a_star(graph, heuristic):
    n = len(graph)
    start = 0
    visited = [False] * n
    path = []
    cost = 0
    f = heuristic[start]

    pq = [(f, start, visited[:], path[:], cost)]

    while pq:
        f, node, visited, path, cost = heapq.heappop(pq)

        if all(visited) and node == start:
            # All nodes have been visited and we have returned to the start node,
            # add the cost of returning to the start node
            path.append(start)
            cost += graph[node][start]
            return path, cost

        for i in range(n):
            if not visited[i] and i != node:
                # Calculate f(n) = g(n) + h(n) for the child node
                g = cost + graph[node][i]
                h = heuristic[i]
                f = g + h

                # Add the child node to the priority queue
                visited[i] = True
                new_path = path + [node]
                heapq.heappush(pq, (f, i, visited[:], new_path[:], g))
                visited[i] = False  # Restore visited flag for the next iteration

    # If no solution found, return None
    return None, float('inf')

# Example graph and heuristics
graph = [[0,12,10,19,8], [12,0,3,7,6], [10,3,0,2,20], [19,7,2,0,4], [8,6,20,4,0]]
heuristic = [0,0,0,0,0]#[29, 18, 21, 11, 17]#[9, 14, 18, 17, 15]

# Solve TSP using A* search
path, cost = tsp_a_star(graph, heuristic)

# Print the optimal path and cost
if path:
    print("Optimal Path:", path)
    print("Optimal Cost:", cost)
else:
    print("No solution found.")