import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

inf = 10 ** 10
edge_list = [[] for _ in range(n + 1)]
for start, end, weight in edges: edge_list[start].append((end, weight))

Result = [inf] * (n + 1)

def dijkstra(start):
    Result[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        dist, curr = heapq.heappop(pq)
        if dist > Result[curr]: continue
        for end, weight in edge_list[curr]:
            if dist + weight < Result[end]:
                Result[end] = dist + weight
                heapq.heappush(pq, (Result[end], end))
    for i in range(2, n + 1): print(-1 if Result[i] == inf else Result[i])

dijkstra(1)