n = int(input())
arr = list(map(int, input().split()))
dp = [0] + [-1] * (n - 1)
result = 0

for i in range(n):
    result = max(result, dp[i])
    if dp[i] == -1: continue
    for j in range(1, arr[i] + 1):
        if i + j >= n: break
        dp[i + j] = max(dp[i + j], dp[i] + 1)

print(result)