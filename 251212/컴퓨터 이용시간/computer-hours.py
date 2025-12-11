import heapq

n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]
p = [interval[0] for interval in intervals]
q = [interval[1] for interval in intervals]

Result = [0] * (n + 1)

List = []
for i, (p, q) in enumerate(intervals):
    List.append((p, 1, i + 1))
    List.append((q, -1, i + 1))
List.sort()

Empty = []
for i in range(1, n + 1): heapq.heappush(Empty, i)

for t, s, p_num in List:
    if s == 1:
        c_num = heapq.heappop(Empty)
        Result[p_num] = c_num
    if s == -1: heapq.heappush(Empty, Result[p_num])

for i in range(1, n + 1): print(Result[i], end = " ")