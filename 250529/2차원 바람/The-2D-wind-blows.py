n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [tuple(map(int, input().split())) for _ in range(q)]
near = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def is_valid(x, y):
    if x < 0 or x >= n or y < 0 or y >= m: return False
    return True

def blow(r1, c1, r2, c2):
    drc = [(0, 1)] * (c2 - c1) + [(1, 0)] * (r2 - r1) + [(0, -1)] * (c2 - c1) + [(-1, 0)] * (r2 - r1)
    x, y = r1, c1
    last_value, now_value = a[x][y], 0
    for dx, dy in drc:
        nx, ny = x + dx, y + dy
        now_value = a[nx][ny]
        a[nx][ny] = last_value
        last_value = now_value
        x, y = nx, ny
    h, w = r2 - r1 + 1, c2 - c1 + 1
    new_arr = [[0] * w for _ in range(h)]
    for di in range(h):
        for dj in range(w):
            i, j = r1 + di, c1 + dj
            Sum, Count = a[i][j], 1
            for dx, dy in near:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m:
                    Sum += a[ni][nj]
                    Count += 1
            new_arr[di][dj] = Sum // Count
    for i in range(h): a[r1 + i][c1:c2 + 1] = new_arr[i]

                
for wind in winds: blow(wind[0] - 1, wind[1] - 1, wind[2] - 1, wind[3] - 1)

for row in a: print(*row)