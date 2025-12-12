n = int(input())

left = 1
right = 0x7FFFFFFFF

Min = 0x7FFFFFFFF
while left <= right:
    mid = (left + right) // 2
    Count = mid - ((mid // 3) + (mid // 5) - (mid // 15))
    if Count >= n:
        Min = min(Min, mid)
        right = mid - 1
    else: left = mid + 1

print(Min)