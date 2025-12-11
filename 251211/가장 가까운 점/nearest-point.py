import heapq

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

queue = []
for x, y in points: heapq.heappush(queue, (x + y, x, y))

for i in range(m):
    a, x, y = heapq.heappop(queue)
    heapq.heappush(queue, (x + y + 4, x + 2, y + 2))

a, x, y = heapq.heappop(queue)
print(x, y)