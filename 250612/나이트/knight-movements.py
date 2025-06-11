n = int(input())
r1, c1, r2, c2 = map(int, input().split())
drc = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
MAX_DIST = 0x7FFFFFFF
Distance = [[MAX_DIST] * n for _ in range(n)]
Distance[r1 - 1][c1 - 1] = 0
Queue = [[r1 - 1, c1 - 1]]
T = 0

while True:
    T += 1
    tmpQueue = []
    for x, y in Queue:
        for dx, dy in drc:
            nx, ny = x + dx, y + dy
            if nx < 0 or n <= nx or ny < 0 or n <= ny: continue
            if T < Distance[nx][ny]:
                Distance[nx][ny] = T
                tmpQueue.append([nx, ny])
    if not tmpQueue: break
    Queue = tmpQueue

print(-1 if Distance[r2 - 1][c2 - 1] == MAX_DIST else Distance[r2 - 1][c2 - 1])