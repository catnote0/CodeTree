n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]

grid = [[0] * n for _ in range(n)]
for x, y in marbles: grid[x - 1][y - 1] = 1

for _ in range(t):
    new_grid = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if grid[x][y]:
                valid_near = [(dx, dy) for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)] if 0 <= x + dx < n and 0 <= y + dy < n]
                rx, ry = max(valid_near, key = lambda d: a[x + d[0]][y + d[1]])
                new_grid[x + rx][y + ry] += 1

    for x in range(n):
        for y in range(n): grid[x][y] = 1 if new_grid[x][y] == 1 else 0

print(sum(sum(row) for row in grid))