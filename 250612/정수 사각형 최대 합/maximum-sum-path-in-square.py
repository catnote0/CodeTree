n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        last_max = 0
        if i > 0: last_max = max(last_max, dp[i - 1][j])
        if j > 0: last_max = max(last_max, dp[i][j - 1])
        dp[i][j] = last_max + grid[i][j]

print(dp[n - 1][n - 1])