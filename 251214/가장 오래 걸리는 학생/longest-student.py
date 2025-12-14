import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

inf = 10 ** 10
edge_list = [[] for _ in range(n + 1)]
for start, end, weight in edges:
    edge_list[start].append((end, weight))
    edge_list[end].append((start, weight))

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
    print(max(Result[1:n]))

dijkstra(n)