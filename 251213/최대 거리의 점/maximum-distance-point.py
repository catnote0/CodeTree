n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()
left = 1
right = 0x7FFFFFFF

Result = 0
while left <= right:
    mid = (left + right) // 2
    last = -0x7FFFFFFF
    Count = 0
    for pos in arr:
        if last + mid <= pos:
            Count += 1
            last = pos
    if Count >= m:
        Result = max(Result, mid)
        left = mid + 1
    else: right = mid - 1

print(Result)