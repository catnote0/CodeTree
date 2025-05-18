n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i, j) == (0, 0): continue
        elif i == 0: grid[i][j] = max(grid[i][j], grid[i][j - 1])
        elif j == 0: grid[i][j] = max(grid[i][j], grid[i - 1][j])
        else: Max = grid[i][j] = max(grid[i][j], min(grid[i - 1][j], grid[i][j - 1]))

print(grid[n - 1][n - 1])