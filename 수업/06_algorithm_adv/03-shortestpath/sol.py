import heapq, math

def dijkstra(graph, start):
    distances = {v:math.inf for v in graph}
    distances[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])
    visited = set()
    visited.add(start)

    while heap:
        # print(heap)
        # print(distances)
        dist, current = heapq.heappop(heap)

        if current in visited and distances[current] < dist : continue
        visited.add(current)

        for next, weight in graph[current].items():
            next_distance = dist + weight
            if next_distance < distances[next]:
                distances[next] = next_distance
                heapq.heappush(heap, [next_distance, next])

    return distances




graph = {
    'a' : {'b':3, 'c':5},
    'b' : {'c':2},
    'c' : {'b':1, 'd':4, 'e':6},
    'd' : {'e':2, 'f':3},
    'e' : {'f':6},
    'f' : {}
}
start_v = 'a'
res = dijkstra(graph, start_v)
print(res)