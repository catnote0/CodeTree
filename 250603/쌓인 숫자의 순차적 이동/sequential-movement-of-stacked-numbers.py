n, m = map(int, input().split())
grid = [[[int(x)] for x in input().split()] for _ in range(n)]
move_nums = list(map(int, input().split()))
near = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def move(num):
    for x in range(n):
        for y in range(n):
            if num in grid[x][y]:
                valid_near = [(dx, dy) for dx, dy in near if 0 <= x + dx < n and 0 <= y + dy < n and grid[x + dx][y + dy]]
                if not valid_near: return
                rx, ry = max(valid_near, key = lambda d: max(grid[x + d[0]][y + d[1]]))
                grid[x + rx][y + ry] += grid[x][y][grid[x][y].index(num):]
                grid[x][y] = grid[x][y][:grid[x][y].index(num)]
                return

for num in move_nums: move(num)

for row in grid:
    for cell in row:
        cell.reverse()
        if not cell: print("None")
        else: print(*cell)