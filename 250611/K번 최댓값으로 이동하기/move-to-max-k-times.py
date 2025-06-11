import sys
sys.setrecursionlimit(10 ** 6)

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1

drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]
visited = []
nr, nc, nv = 0, 0, 0

def search(x, y, value):
    global nr, nc, nv
    for dx, dy in drc:
        nx, ny = x + dx, y + dy
        if nx < 0 or n <= nx or ny < 0 or n <= ny: continue
        if visited[nx][ny] or grid[nx][ny] >= value: continue
        visited[nx][ny] = True
        if nv < grid[nx][ny]: nr, nc, nv = nx, ny, grid[nx][ny]
        elif nv == grid[nx][ny]:
            if nx < nr: nr, nc, nv = nx, ny, grid[nx][ny]
            elif nx == nr:
                if ny < nc: nr, nc, nv = nx, ny, grid[nx][ny]
        search(nx, ny, value)

for _ in range(k):
    visited = [[False] * n for _ in range(n)]
    nr, nc, nv = r, c, 0
    search(r, c, grid[r][c])
    r, c = nr, nc

print(r + 1, c + 1)