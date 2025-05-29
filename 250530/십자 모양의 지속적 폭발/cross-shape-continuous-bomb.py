n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input()) for _ in range(m)]
drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def Explode(y):
    x = -1
    for i in range(n):
        if grid[i][y]:
            x = i
            break
    if x == -1: return
    size = grid[x][y]
    grid[x][y] = 0
    for dx, dy in drc:
        for i in range(1, size):
            nx, ny = x + dx * i, y + dy * i
            if 0 <= nx < n and 0 <= ny < n: grid[nx][ny] = 0
            else: break

def drop():
    after_drop = [[0] * n for _ in range(n)]
    for i in range(n):
        pos = n - 1
        for j in range(n - 1, -1, -1):
            if not grid[j][i]: continue
            after_drop[pos][i] = grid[j][i]
            pos -= 1
    for i in range(n): grid[i] = after_drop[i][:]

for column in commands:
    Explode(column - 1)
    drop()

for row in grid: print(*row)