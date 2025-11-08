n, m = map(int, input().split())
points = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]

points.sort()

def binary_search(value, flag):
    pos = flag * 0x7FFFFFFF
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if flag > 0:
            if value <= points[mid]:
                pos = min(pos, mid)
                right = mid - 1
            else: left = mid + 1
        else:
            if points[mid] <= value:
                pos = max(pos, mid)
                left = mid + 1
            else: right = mid - 1
    return pos


for start, end in segments:
    left = binary_search(start, 1)
    right = binary_search(end, -1)
    print(0 if abs(right - left + 1) > n else right - left + 1)