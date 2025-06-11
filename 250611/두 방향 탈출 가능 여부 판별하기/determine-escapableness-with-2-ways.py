n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def search(x, y):
    if x == n - 1 and y == m - 1:
        print(1)
        exit(0)
    if 0 <= x < n and 0 <= y + 1 < m and grid[x][y + 1]: search(x, y + 1)
    if 0 <= x + 1 < n and 0 <= y < m and grid[x + 1][y]: search(x + 1, y)

search(0, 0)
print(0)