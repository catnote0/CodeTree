import heapq

n = int(input())
arr = list(map(int, input().split()))

queue = []
for a in arr: heapq.heappush(queue, -a)

while True:
    if len(queue) == 1:
        print(-queue[0])
        exit(0)
    if len(queue) == 0:
        print(-1)
        exit(0)
    a = -heapq.heappop(queue)
    b = -heapq.heappop(queue)
    if a != b: heapq.heappush(queue, -(a - b))