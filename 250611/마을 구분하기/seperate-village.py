n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]
color_count = []
def fill(x, y, c):
    grid[x][y] = c
    color_count[-c - 1] += 1
    for dx, dy in drc:
        nx, ny = x + dx, y + dy
        if nx < 0 or n <= nx or ny < 0 or n <= ny: continue
        if grid[nx][ny] == 1: fill(nx, ny, c)

color = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            color -= 1
            color_count.append(0)
            fill(i, j, color)

print(-color)
color_count.sort()
for c in color_count: print(c)