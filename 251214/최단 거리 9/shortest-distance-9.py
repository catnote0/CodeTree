import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())

inf = 10 ** 10
edge_list = [[] for _ in range(n + 1)]
for start, end, weight in edges:
    edge_list[start].append((end, weight))
    edge_list[end].append((start, weight))

Result = [[inf, -1] for _ in range(n + 1)]

def dijkstra(start):
    Result[start][0] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        dist, curr = heapq.heappop(pq)
        if dist > Result[curr][0]: continue
        for end, weight in edge_list[curr]:
            if dist + weight < Result[end][0]:
                Result[end][0] = dist + weight
                Result[end][1] = curr
                heapq.heappush(pq, (Result[end][0], end))
    Route = []
    curr = B
    while curr != -1:
        Route.append(curr)
        curr = Result[curr][1]
    Route.reverse()
    print(Result[B][0])
    for r in Route: print(r, end = " ")

dijkstra(A)