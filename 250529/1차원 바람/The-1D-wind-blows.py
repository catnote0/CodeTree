n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

def Spread(row, Sdrc, drc):
    if row < 0 or row >= n: return
    StopSpread = True
    for i in range(m):
        if a[row][i] == a[row + (-1 if Sdrc == 'D' else 1)][i]: StopSpread = False
    if StopSpread: return
    a[row] = (a[row][(m - 1):] + a[row][:(m - 1)]) if drc == 'L' else (a[row][1:] + a[row][:1])
    Spread(row + (1 if Sdrc == 'D' else -1), Sdrc, 'R' if drc == 'L' else 'L')

def Blow(wind):
    (row, drc) = (wind[0] - 1, wind[1])
    a[row] = (a[row][(m - 1):] + a[row][:(m - 1)]) if drc == 'L' else (a[row][1:] + a[row][:1])
    Spread(row + 1, 'D', 'R' if drc == 'L' else 'L')
    Spread(row - 1, 'U', 'R' if drc == 'L' else 'L')

for wind in winds: Blow(wind)

for row in a: print(*row)