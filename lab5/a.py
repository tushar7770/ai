# import heapq

# def a_star(graph, start, heuristic_factor):
#     n = len(graph)
#     dist = [float('inf')] * n
#     visited = [False] * n
#     parent = [None] * n
#     heap = []
#     heapq.heappush(heap, (0, start))
#     dist[start] = 0
#     while heap:
#         g, u = heapq.heappop(heap)
#         if visited[u]:
#             continue
#         visited[u] = True
#         for v, edge_weight in enumerate(graph[u]):
#             if visited[v]:
#                 continue
#             f = g + edge_weight + heuristic_factor[v] - heuristic_factor[u]
#             if dist[v] > f:
#                 dist[v] = f
#                 heapq.heappush(heap, (f, v))
#                 parent[v] = u
#     return parent

# def tsp_tour_cost(graph, parent):
#     cost = 0
#     for i, p in enumerate(parent):
#         if p is None:
#             continue
#         cost += graph[p][i]
#     return cost

# if __name__ == "__main__":
#     graph = [[ 0, 12, 10, 19, 8],
#              [ 12, 0 , 3 ,7, 6],
#              [ 10, 3 , 0 , 2, 20],
#              [ 19, 7 , 2  ,0, 4],
#              [ 8, 6, 20, 4, 0]]

#     heuristic_factor = [0,0,0,0,0]
#     parent = a_star(graph, 0, heuristic_factor)
#     cost = tsp_tour_cost(graph, parent)
#     print(f"Minimum TSP tour cost: {cost}")


import heapq
import math
import numpy as np

def heuristic_cost(graph, remaining_nodes, current_node, minimum_spanning_tree_cost):
    """
    Calculates the heuristic cost of remaining nodes using the minimum cost spanning tree approach.
    """
    return minimum_spanning_tree_cost + sum(graph[current_node][j] for j in remaining_nodes)

def a_star_tsp(graph, start_node):
    """
    Implements the A* algorithm to solve the TSP problem.
    """
    n = len(graph)
    print(n)
    closed_set = set()
    open_set = [(0, start_node, [])]
    minimum_spanning_tree_cost = 0

    while open_set:
        f, current_node, path = heapq.heappop(open_set)

        if len(path) == n - 1:
            return path + [current_node]

        closed_set.add(current_node)

        remaining_nodes = set(range(n)) - set(path + [current_node])
        for j in remaining_nodes:
            if j not in closed_set:
                g = f - heuristic_cost(graph, remaining_nodes, current_node, minimum_spanning_tree_cost) + graph[current_node][j]
                h = heuristic_cost(graph, remaining_nodes, j, minimum_spanning_tree_cost)
                heapq.heappush(open_set, (g + h, j, path + [current_node]))
        print(path)

    return path

if __name__ == '_main_':
    arr = [[0, 12, 10, 19,8], [12, 0, 3,7,6], [10, 3, 0, 2,20], [19,7,2,0,4],[8,6,20,4,0]]
    arr2=[[0, 2, 9, 10], [1, 0, 6, 4], [15, 7, 0, 8], [6, 3, 12, 0]]
    arr3 = [[0, 12, 10, 19], [12, 0, 3,7], [10, 3, 0, 2], [19,7,2,0]]
    graph = np.array(arr)
    start_node = 0
    path = a_star_tsp(graph, start_node)
    print("The minimum weight for traveling salesman to visit all the nodes:", sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1)))
    print("The shortest path to visit every city:", path)