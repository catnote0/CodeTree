m = int(input())
a, b = map(int, input().split())

Min = 0x7FFFFFFF
Max = 0
for num in range(a, b + 1):
    left = 1
    right = m
    count = 0
    while left <= right:
        mid = (left + right) // 2
        count += 1
        if num < mid: right = mid - 1
        elif num > mid: left = mid + 1
        else: break
    Min = min(Min, count)
    Max = max(Max, count)

print(Min, Max)