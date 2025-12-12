n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

left = 1
right = 0x7FFFFFFFFFFF

Min = 0x7FFFFFFFFFFF
while left <= right:
    mid = (left + right) // 2
    Count = 0
    for r in arr: Count += mid // r
    if Count >= n:
        Min = min(Min, mid)
        right = mid - 1
    else: left = mid + 1

print(Min)