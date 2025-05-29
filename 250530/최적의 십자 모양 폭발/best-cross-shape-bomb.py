n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]
Max = 0

def Explode(x, y):
    global Max
    new_grid = []
    for i in range(n): new_grid.append(grid[i][:])
    size = new_grid[x][y]
    new_grid[x][y] = 0
    for dx, dy in drc:
        for i in range(1, size):
            nx, ny = x + dx * i, y + dy * i
            if 0 <= nx < n and 0 <= ny < n: new_grid[nx][ny] = 0
            else: break
    Result = [[0] * n for _ in range(n)]
    for i in range(n):
        pos = n - 1
        for j in range(n - 1, -1, -1):
            if not new_grid[j][i]: continue
            Result[pos][i] = new_grid[j][i]
            pos -= 1
    count = 0
    for i in range(n):
        for j in range(n - 1):
            if Result[i][j] and Result[i][j] == Result[i][j + 1]: count += 1
            if Result[j][i] and Result[j][i] == Result[j + 1][i]: count += 1
    Max = max(Max, count)

for i in range(n):
    for j in range(n): Explode(i, j)

print(Max)