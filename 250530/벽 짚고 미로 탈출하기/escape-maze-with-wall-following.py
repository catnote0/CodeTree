N = int(input())
x, y = map(int, input().split())
grid = [['X'] * (N + 2) for _ in range(N + 2)]

FORWARD = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
RIGHT = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
DRC = ['U', 'R', 'D', 'L']
WALL = '#'
EXIT = 'X'

for i in range(1, N + 1):
    row = input()
    for j in range(1, N + 1):
        grid[i][j] = row[j - 1]
drc = 'R'

def check_isolated(x, y):
    for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        if grid[x + dx][y + dy] != WALL: return
    print(-1)
    exit(0)

def get_forward(x, y, drc):
    dx, dy = FORWARD[drc]
    return (x + dx, y + dy)

def get_right(x, y, drc):
    dx, dy = RIGHT[drc]
    return (x + dx, y + dy)

def go_forward(x, y, drc):
    dx, dy = FORWARD[drc]
    return (x + dx, y + dy)

def turn(where, drc):
    if where == 'Right': return DRC[(DRC.index(drc) + 1) % 4]
    return DRC[DRC.index(drc) - 1]

check_isolated(x, y)
time = 0
while True:
    if time > 10000:
        print(-1)
        exit(0)
    if grid[x][y] == EXIT:
        print(time)
        exit(0)
    rx, ry = get_right(x, y, drc)
    if grid[rx][ry] != WALL: drc = turn('Right', drc)
    else:
        while True:
            fx, fy = get_forward(x, y, drc)
            if grid[fx][fy] == WALL: drc = turn('LEFT', drc)
            else: break
    x, y = go_forward(x, y, drc)
    time += 1