import heapq

n = int(input())
x = [int(input()) for _ in range(n)]

queue = []

for a in x:
    if a == 0:
        if not queue: print(0)
        else: print(heapq.heappop(queue))
    else: heapq.heappush(queue, a)