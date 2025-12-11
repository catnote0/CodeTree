import heapq

n = int(input())
arr = list(map(int, input().split()))

queue = []

for a in arr:
    heapq.heappush(queue, -a)
    if len(queue) < 3: print(-1)
    else:
        if len(queue) > 3: heapq.heappop(queue)
        print(-queue[0] * queue[1] * queue[2])