n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [tuple(map(int, input().split())) for _ in range(q)]

def is_valid(x, y):
    if x < 0 or x >= n or y < 0 or y >= m: return False
    return True

def blow(r1, c1, r2, c2):
    drc = [(0, 1)] * (c2 - c1) + [(1, 0)] * (r2 - r1) + [(0, -1)] * (c2 - c1) + [(-1, 0)] * (r2 - r1)
    near = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    x, y = r1, c1
    last_value, now_value = a[x][y], 0
    for (dx, dy) in drc:
        now_value = a[x + dx][y + dy]
        a[x + dx][y + dy] = last_value
        last_value = now_value
        (x, y) = (x + dx, y + dy)
    new_arr = [[0] * m for _ in range(n)]
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            Sum, Count = a[i][j], 1
            for (dx, dy) in near:
                if is_valid(i + dx, j + dy):
                    Sum += a[i + dx][j + dy]
                    Count += 1
            new_arr[i][j] = Sum // Count
    for i in range(r1, r2 + 1): a[i][c1:(c2 + 1)] = new_arr[i][c1:(c2 + 1)]

                
for wind in winds: blow(wind[0] - 1, wind[1] - 1, wind[2] - 1, wind[3] - 1)

for row in a: print(*row)