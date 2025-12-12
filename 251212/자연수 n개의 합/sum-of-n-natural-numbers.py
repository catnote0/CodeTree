s = int(input())

left = 1
right = 0x7FFFFFFF

Max = 0
while left <= right:
    mid = (left + right) // 2
    Sum = mid * (mid + 1) // 2
    if Sum <= s:
        Max = max(Max, mid)
        left = mid + 1
    else: right = mid - 1

print(Max)