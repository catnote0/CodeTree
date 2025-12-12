import heapq

n = int(input())
arr = list(map(int, input().split()))

queue = []
for a in arr: heapq.heappush(queue, a)

Result = 0
for i in range(n - 1):
    a = heapq.heappop(queue)
    b = heapq.heappop(queue)
    Result += (a + b)
    heapq.heappush(queue, a + b)

print(Result)