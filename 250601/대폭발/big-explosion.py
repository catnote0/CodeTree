n, m, r, c = map(int, input().split())

grid = [[0] * n for _ in range(n)]
r, c = r - 1, c - 1
grid[r][c] = 1
drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def explode(t):
    new_grid = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if grid[x][y]:
                new_grid[x][y] = 1
                for dx, dy in drc:
                    nx, ny = x + dx * (2 ** (t - 1)), y + dy * (2 ** (t - 1))
                    if 0 <= nx < n and 0 <= ny < n: new_grid[nx][ny] = 1
    for i in range(n): grid[i] = new_grid[i][:]

for t in range(1, m + 1):
    explode(t)

print(sum(sum(row) for row in grid))