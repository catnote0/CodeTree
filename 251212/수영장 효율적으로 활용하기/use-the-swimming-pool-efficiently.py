n, m = map(int, input().split())
T = list(map(int, input().split()))

left = max(T)
right = sum(T)

Min = 0x7FFFFFFF
while left <= right:
    mid = (left + right) // 2
    Count = 1
    Sum = 0
    for t in T:
        if Sum + t <= mid: Sum += t
        else:
            Sum = t
            Count += 1
    if Count <= m:
        Min = min(Min, mid)
        right = mid - 1
    else: left = mid + 1

print(Min)