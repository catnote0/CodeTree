n, m, t = map(int, input().split())

r, c, d, w = [], [], [], []
for _ in range(m):
    ri, ci, di, wi = input().split()
    r.append(int(ri) - 1)
    c.append(int(ci) - 1)
    d.append(di)
    w.append(int(wi))

live = [True] * m
drc = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

def move(r, c, d):
    if d == 'L' and c == 0: d = 'R'
    elif d == 'R' and c == n - 1: d = 'L'
    elif d == 'U' and r == 0: d = 'D'
    elif d == 'D' and r == n - 1: d = 'U'
    else: r, c = r + drc[d][0], c + drc[d][1]
    return (r, c, d)

for _ in range(t):
    grid = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(m):
        if not live[i]: continue
        r[i], c[i], d[i] = move(r[i], c[i], d[i])
        grid[r[i]][c[i]].append((i, w[i], d))
    for row in grid:
        for cell in row:
            if len(cell) > 1:
                weight = sum(bead[1] for bead in cell)
                winner = max(bead[0] for bead in cell)
                for bead in cell:
                    if bead[0] != winner: live[bead[0]] = False
                w[winner] = weight

print(sum(live), max(w[i] for i in range(n) if live[i]))