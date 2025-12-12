n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

left = 1
right = 100000

Result = 0
while left <= right:
    mid = (left + right) // 2
    Count = 0
    for num in arr: Count += num // mid
    if Count >= m:
        Result = max(Result, mid)
        left = mid + 1
    else: right = mid - 1

print(Result)