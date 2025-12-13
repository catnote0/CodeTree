import heapq

N, T_max = map(int, input().split())
d = [int(input()) for _ in range(N)]

left = 1
right = N

Result = 0x7FFFFFFF
while left <= right:
    mid = (left + right) // 2
    pq = []
    Max = 0
    for i in range(mid):
        heapq.heappush(pq, d[i])
        Max = max(Max, d[i])
    for i in range(mid, N):
        t = heapq.heappop(pq)
        heapq.heappush(pq, t + d[i])
        Max = max(Max, t + d[i])
    if Max <= T_max:
        Result = min(Result, mid)
        right = mid - 1
    else: left = mid + 1

print(Result)