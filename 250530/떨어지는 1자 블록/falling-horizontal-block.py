n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

for r in range(n):
    for c in range(k - 1, k + m - 1):
        if grid[r][c]:
            grid[r - 1][k - 1:k + m - 1] = [1] * m
            for row in grid: print(*row)
            exit(0)

grid[n - 1][k - 1:k + m - 1] = [1] * m
for row in grid: print(*row)