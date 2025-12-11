import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))

queue = []
for a in arr: heapq.heappush(queue, -a)

for i in range(m):
    a = heapq.heappop(queue)
    heapq.heappush(queue, a + 1)

print(-queue[0])