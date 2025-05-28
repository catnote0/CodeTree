n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())
r -= 1
c -= 1
rotate_arr = [[-1, 1]] * m1 + [[-1, -1]] * m2 + [[1, -1]] * m3 + [[1, 1]] * m4
if dir:
    rotate_arr = [[-x for x in rotate] for rotate in rotate_arr]
    rotate_arr.reverse()

last_value = grid[r][c]
for dx, dy in rotate_arr:
    now_value = grid[r + dx][c + dy]
    grid[r + dx][c + dy] = last_value
    last_value = now_value
    r += dx
    c += dy

for row in grid: print(*row)