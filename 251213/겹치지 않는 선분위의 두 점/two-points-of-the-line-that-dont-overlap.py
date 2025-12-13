n, m = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(m)]

segments.sort(key = lambda x: x[0])

inf = 0x7FFFFFFFFFFFFFFF
left = 1
right = inf

Result = 0
while left <= right:
    mid = (left + right) // 2
    Count = 0
    last = -inf
    for segment in segments:
        if last + mid > segment[1]: continue
        first_pos = max(segment[0], last + mid)
        n_dot = (segment[1] - first_pos) // mid + 1
        last = first_pos + mid * (n_dot - 1)
        Count += n_dot
    if Count >= n:
        Result = max(Result, mid)
        left = mid + 1
    else: right = mid - 1
print(Result)
        