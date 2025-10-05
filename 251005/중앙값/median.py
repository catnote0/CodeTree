import heapq

t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))
    large = []
    small = []

    heapq.heappush(large, arr[0])
    print(large[0], end = " ")

    for i in range(1, m):
        n = arr[i]
        if i % 2 == 0:
            if -small[0] <= n: heapq.heappush(large, n)
            else:
                heapq.heappush(large, -heapq.heappop(small))
                heapq.heappush(small, -n)
            print(large[0], end = " ")
        else:
            if large[0] >= n: heapq.heappush(small, -n)
            else:
                heapq.heappush(small, -heapq.heappop(large))
                heapq.heappush(large, n)
    print()