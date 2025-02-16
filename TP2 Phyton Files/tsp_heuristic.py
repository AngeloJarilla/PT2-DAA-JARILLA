# 7) Heuristic Method - Traveling Salesman Approximation
def nearest_neighbor_tsp(graph, start):
    unvisited = set(graph.keys())
    unvisited.remove(start)
    tour = [start]
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda city: graph[last][city])
        tour.append(next_city)
        unvisited.remove(next_city)
    return tour

graph = {0: {1: 10, 2: 15, 3: 20},
         1: {0: 10, 2: 35, 3: 25},
         2: {0: 15, 1: 35, 3: 30},
         3: {0: 20, 1: 25, 2: 30}}

print("TSP Approximate Tour:", nearest_neighbor_tsp(graph, 0))
