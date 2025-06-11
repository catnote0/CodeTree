n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r - 1, c - 1
drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]
visited = [[False] * n for _ in range(n)]

for _ in range(k):
    Queue = [[r, c]]
    v, nr, nc, nv = grid[r][c], r, c, 0
    while True:
        tmpQueue = []
        for x, y in Queue:
            for dx, dy in drc:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                if visited[nx][ny] or grid[nx][ny] >= v: continue
                if (grid[nx][ny], -nx, -ny) > (nv, -nr, -nc): nr, nc, nv = nx, ny, grid[nx][ny]
                visited[nx][ny] = True
                tmpQueue.append([nx, ny])
        if not tmpQueue: break
        Queue = tmpQueue
    r, c = nr, nc
    for i in range(n):
        for j in range(n): visited[i][j] = False

print(r + 1, c + 1)