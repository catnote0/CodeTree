n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

for q in queries:
    left = 0
    right = n - 1
    Found = False
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < q: left = mid + 1
        elif arr[mid] > q: right = mid - 1
        else:
            Found = True
            print(mid + 1)
            break
    if not Found: print(-1)