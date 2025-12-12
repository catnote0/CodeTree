n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

Dict = {}

Result = -1
for i in range(n):
    if i > k: Dict[arr[i - k - 1]] -= 1
    if arr[i] in Dict and Dict[arr[i]] > 0: Result = max(Result, arr[i])
    Dict[arr[i]] = Dict[arr[i]] + 1 if arr[i] in Dict else 1

print(Result)