import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

inf = 10**10
edges.sort()
edge_info = [-1] * (n + 2)
for i, (s, _, _) in enumerate(edges): edge_info[s] = i if edge_info[s] == -1 else edge_info[s]
edge_info[n + 1] = m
for i in range(n, 0, -1): edge_info[i] = edge_info[i + (1 if edge_info[i] == -1 else 0)]

Result = [inf] * (n + 1)

def dijkstra(start):
    Result[start] = 0
    pq = []
    for i in range(1, n + 1): heapq.heappush(pq, (Result[i], i))
    while pq:
        dist, pos = heapq.heappop(pq)
        if dist > Result[pos]: continue
        for i in range(edge_info[pos], edge_info[pos + 1]):
            s, e, v = edges[i]
            if dist + v < Result[e]:
                Result[e] = dist + v
                heapq.heappush(pq, (Result[e], e))
    for i in range(1, n + 1):
        if i == start: continue
        print(-1 if Result[i] == inf else Result[i])

dijkstra(1)