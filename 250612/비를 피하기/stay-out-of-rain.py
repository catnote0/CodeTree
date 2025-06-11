n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]
MAX_DIST = 0x7FFFFFFF
Distance = [[MAX_DIST] * n for _ in range(n)]
Queue = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 3:
            Queue.append([i, j])
            Distance[i][j] = 0

T = 0
while True:
    T += 1
    tmpQueue = []
    for x, y in Queue:
        for dx, dy in drc:
            nx, ny = x + dx, y + dy
            if nx < 0 or n <= nx or ny < 0 or n <= ny: continue
            if grid[nx][ny] == 1: continue
            if T < Distance[nx][ny]:
                Distance[nx][ny] = T
                tmpQueue.append([nx, ny])
    if not tmpQueue: break
    Queue = tmpQueue

for i in range(n):
    row = []
    for j in range(n):
        if grid[i][j] != 2: row.append(0)
        else: row.append(-1 if Distance[i][j] == MAX_DIST else Distance[i][j])
    print(*row)