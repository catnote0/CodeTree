n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

result = 1000

def has_route(low, high):
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][j] = low <= grid[i][j] <= high
            if i == 0 and j > 0: dp[i][j] = dp[i][j] and dp[i][j - 1]
            if i > 0 and j == 0: dp[i][j] = dp[i][j] and dp[i - 1][j]
            if i > 0 and j > 0: dp[i][j] = dp[i][j] and (dp[i - 1][j] or dp[i][j - 1])
    return dp[n - 1][n - 1]

for low in range(1, 101):
    for high in range(low, 101):
        if has_route(low, high): result = min(result, (high - low))

print(result)