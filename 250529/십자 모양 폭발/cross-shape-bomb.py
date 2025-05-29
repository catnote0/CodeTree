n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def Explode(x, y):
    size = grid[x][y]
    grid[x][y] = 0
    for dx, dy in drc:
        for i in range(1, size):
            nx, ny = x + dx * i, y + dy * i
            if 0 <= nx < n and 0 <= ny < n: grid[nx][ny] = 0
            else: break

Explode(r - 1, c - 1)

Result = [[0] * n for _ in range(n)]
for i in range(n):
    pos = n - 1
    for j in range(n - 1, -1, -1):
        if not grid[j][i]: continue
        Result[pos][i] = grid[j][i]
        pos -= 1

for row in Result: print(*row)