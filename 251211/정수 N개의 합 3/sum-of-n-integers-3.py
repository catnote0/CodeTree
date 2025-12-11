n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0: continue
        elif i == 0: arr[i][j] += arr[i][j - 1]
        elif j == 0: arr[i][j] += arr[i - 1][j]
        else: arr[i][j] += (arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1])

Result = 0

for i in range(k - 1, n):
    for j in range(k - 1, n):
        if i == k - 1 and j == k - 1: Result = arr[i][j]
        elif i == k - 1: Result = max(Result, arr[i][j] - arr[i][j - k])
        elif j == k - 1: Result = max(Result, arr[i][j] - arr[i - k][j])
        else: Result = max(Result, arr[i][j] - arr[i][j - k] - arr[i - k][j] + arr[i - k][j - k])

print(Result)