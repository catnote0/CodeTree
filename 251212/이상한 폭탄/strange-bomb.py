n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

Count = [0] * 1100000

Result = -1
for i in range(n):
    if i > k: Count[arr[i - k - 1]] -= 1
    if Count[arr[i]]: Result = max(Result, arr[i])
    Count[arr[i]] += 1

print(Result)