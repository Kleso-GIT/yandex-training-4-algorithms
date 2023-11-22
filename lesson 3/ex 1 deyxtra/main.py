# https://contest.yandex.ru/contest/53031/problems/A/

import heapq

n, s, f = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

distances = [float('inf')] * n
distances[s - 1] = 0

priority_queue = [(0, s - 1)]
while priority_queue:
    current_distance, current_vertex = heapq.heappop(priority_queue)

    if current_distance > distances[current_vertex]:
        continue

    for neighbor, weight in enumerate(matrix[current_vertex]):
        if weight > 0:
            distance_to_neighbor = current_distance + weight
            if distance_to_neighbor < distances[neighbor]:
                distances[neighbor] = distance_to_neighbor
                heapq.heappush(priority_queue, (distance_to_neighbor, neighbor))

if distances[f - 1] == float('inf'):
    print(-1)
else:
    print(distances[f - 1])
