from collections import deque

spread_dir = {'D': 1, 'U': -1}
wind_dir = {'L': 1, 'R': -1}
oppo = {'L': 'R', 'R': 'L'}

n, m, q = map(int, input().split())
a = [deque(list(map(int, input().split()))) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

def Spread(row, Sdrc, drc):
    while True:
        if row < 0 or row >= n: return
        if not any(x == y for x, y in zip(a[row], a[row - spread_dir[Sdrc]])): return
        a[row].rotate(wind_dir[drc])
        row += spread_dir[Sdrc]
        drc = oppo[drc]

def Blow(wind):
    (row, drc) = (wind[0] - 1, wind[1])
    a[row].rotate(wind_dir[drc])
    Spread(row + 1, 'D', oppo[drc])
    Spread(row - 1, 'U', oppo[drc])

for wind in winds: Blow(wind)

for row in a: print(*row)