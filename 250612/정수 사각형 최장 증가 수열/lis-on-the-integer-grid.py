import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]
dfs_grid = [[-1] * n for _ in range(n)]
result = 0

def dfs(x, y):
    if dfs_grid[x][y] != -1: return dfs_grid[x][y]
    max_dist = 0
    for dx, dy in drc:
        nx, ny = x + dx, y + dy
        if nx < 0 or n <= nx or ny < 0 or n <= ny: continue
        if grid[nx][ny] >= grid[x][y]: continue
        max_dist = max(max_dist, dfs(nx, ny))
    dfs_grid[x][y] = max_dist + 1
    return dfs_grid[x][y]

for i in range(n):
    for j in range(n):
        if dfs_grid[i][j] == -1: result = max(result, dfs(i, j))

print(result)