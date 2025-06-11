n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n - 1, -1, -1):
        if i == 0 and j == n - 1:
            dp[i][j] = grid[i][j]
            continue
        if i == 0: dp[i][j] = dp[i][j + 1] + grid[i][j]
        elif j == n - 1: dp[i][j] = dp[i - 1][j] + grid[i][j]
        else: dp[i][j] = min(dp[i - 1][j], dp[i][j + 1]) + grid[i][j]

print(dp[n - 1][0])