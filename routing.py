import heapq

def dijkstra(graph, start, end):
    queue = [(0, start)]
    distances = {start: 0}
    visited = set()

    while queue:
        cost, node = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)
        for neighbor, pollution in graph.get(node, []):
            new_cost = cost + pollution
            if neighbor not in distances or new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor))

    return distances.get(end, float("inf"))
