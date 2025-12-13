n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

segments.sort(key = lambda x: x[0])

left = 1
right = 10**9

Result = 0
while left <= right:
    mid = (left + right) // 2
    last = -10**9
    Possible = True
    for a, b in segments:
        if last + mid > b:
            Possible = False
            break
        last = max(last + mid, a)
    if Possible:
        Result = max(Result, mid)
        left = mid + 1
    else: right = mid - 1

print(Result)