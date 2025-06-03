n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

scope_list = [[(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)], [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)], [(-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)]]
bomb_list = []

for i in range(n):
    for j in range(n):
        if grid[i][j]: bomb_list.append([i, j])

n_bomb = len(bomb_list)
effect_map = [[0] * n for _ in range(n)]
Result = 0

def explode(num):
    global Result
    if num == n_bomb:
        Result = max(Result, sum(sum(1 if cell else 0 for cell in row) for row in effect_map))
        return
    x, y = bomb_list[num]
    for scope in scope_list:
        for dx, dy in scope:
            if 0 <= x + dx < n and 0 <= y + dy < n: effect_map[x + dx][y + dy] += 1
        explode(num + 1)
        for dx, dy in scope:
            if 0 <= x + dx < n and 0 <= y + dy < n: effect_map[x + dx][y + dy] -= 1

explode(0)
print(Result)