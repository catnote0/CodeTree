n, m, t, k = map(int, input().split())

r, c, d, v = [], [], [], []
for _ in range(m):
    ri, ci, di, vi = input().split()
    r.append(int(ri) - 1)
    c.append(int(ci) - 1)
    d.append(di)
    v.append(int(vi))

live = [True] * m
drc = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

def move(r, c, d, v):
    for _ in range(v):
        if d == 'L' and c == 0: d = 'R'
        elif d == 'R' and c == n - 1: d = 'L'
        elif d == 'U' and r == 0: d = 'D'
        elif d == 'D' and r == n - 1: d = 'U'
        r, c = r + drc[d][0], c + drc[d][1]
    return (r, c, d)

for T in range(t):
    grid = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(m):
        if not live[i]: continue
        r[i], c[i], d[i] = move(r[i], c[i], d[i], v[i])
        grid[r[i]][c[i]].append((v[i], i))
    for row in grid:
        for cell in row:
            if len(cell) > k:
                cell.sort(reverse = True)
                for bead in cell[k:]: live[bead[1]] = False

print(sum(live))