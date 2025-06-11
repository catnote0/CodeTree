n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]
check = []

def fill(x, y, h):
    check[x][y] = True
    for dx, dy in drc:
        nx, ny = x + dx, y + dy
        if nx < 0 or n <= nx or ny < 0 or m <= ny: continue
        if grid[nx][ny] > h and not check[nx][ny]: fill(nx, ny, h)

result = 0
result_K = 0

for K in range(1, 100):
    check = [[False] * m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > K and not check[i][j]:
                count += 1
                fill(i, j, K)
    if result < count:
        result = count
        result_K = K

print(result_K, result)