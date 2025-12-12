import bisect

n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

for q in query:
    pos = bisect.bisect_left(arr, q)
    if arr[pos] != q: print(-1)
    else: print(pos + 1)