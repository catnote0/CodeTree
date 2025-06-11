n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
result = 1

dp = [[-0x7FFFFFF] * m for _ in range(n)]
dp[0][0] = 1

for i in range(1, n):
    for j in range(1, n):
        for k in range(i):
            for l in range(j):
                if grid[i][j] <= grid[k][l]: continue
                dp[i][j] = max(dp[i][j], dp[k][l] + 1)
                result = max(result, dp[i][j])
print(result)