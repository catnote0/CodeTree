import heapq

n = int(input())
price = list(map(int, input().split()))

List = [1]

Result = 0
for i in range(n - 1, -1, -1):
    Result = max(Result, -List[0] - price[i])
    heapq.heappush(List, -price[i])

print(Result)