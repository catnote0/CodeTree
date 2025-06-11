import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]
block_count = 0
cell_count = 0
max_block = 0

def search(x, y, value):
    global cell_count
    visited[x][y] = True
    for dx, dy in drc:
        nx, ny = x + dx, y + dy
        if nx < 0 or n <= nx or ny < 0 or n <= ny: continue
        if grid[nx][ny] == value and not visited[nx][ny]:
            cell_count += 1
            search(nx, ny, value)

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cell_count = 1
            search(i, j, grid[i][j])
            max_block = max(max_block, cell_count)
            if cell_count >= 4: block_count += 1

print(block_count, max_block)