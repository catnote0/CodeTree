grid = [list(map(int, input().split())) for _ in range(4)]
drc = input()
n = 4

def drop():
    global grid
    after_drop = [[0] * n for _ in range(n)]
    if drc == 'D':
        for i in range(n):
            pos = n - 1
            for j in range(n - 1, -1, -1):
                if not grid[j][i]: continue
                after_drop[pos][i] = grid[j][i]
                pos -= 1
    if drc == 'U':
        for i in range(n):
            pos = 0
            for j in range(n):
                if not grid[j][i]: continue
                after_drop[pos][i] = grid[j][i]
                pos += 1
    if drc == 'R':
        for i in range(n):
            pos = n - 1
            for j in range(n - 1, -1, -1):
                if not grid[i][j]: continue
                after_drop[i][pos] = grid[i][j]
                pos -= 1
    if drc == 'L':
        for i in range(n):
            pos = 0
            for j in range(n):
                if not grid[i][j]: continue
                after_drop[i][pos] = grid[i][j]
                pos += 1
    for i in range(n): grid[i] = after_drop[i][:]
    
def merge():
    if drc == 'D':
        for i in range(n):
            for j in range(n - 1, 0, -1):
                if grid[j][i] == grid[j - 1][i]:
                    grid[j][i] *= 2
                    grid[j - 1][i] = 0
                    j -= 1
    if drc == 'U':
        for i in range(n):
            for j in range(n - 1):
                if grid[j][i] == grid[j + 1][i]:
                    grid[j][i] *= 2
                    grid[j + 1][i] = 0
                    j += 1
    if drc == 'R':
        for i in range(n):
            for j in range(n - 1, 0, -1):
                if grid[i][j] == grid[i][j - 1]:
                    grid[i][j] *= 2
                    grid[i][j - 1] = 0
                    j -= 1
    if drc == 'L':
        for i in range(n):
            for j in range(n - 1):
                if grid[i][j] == grid[i][j + 1]:
                    grid[i][j] *= 2
                    grid[i][j + 1] = 0
                    j += 1

drop()
merge()
drop()

for row in grid: print(*row)