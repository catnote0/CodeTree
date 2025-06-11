n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]
Visited = [[False] * m for _ in range(n)]
ice = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 1: ice += 1

def fill(x, y):
    Queue = [[x, y]]
    for i in range(n):
        for j in range(m): Visited[i][j] = False
    a[x][y] = -1
    Visited[x][y] = True
    while True:
        tmpQueue = []
        for x, y in Queue:
            for dx, dy in drc:
                nx, ny = x + dx, y + dy
                if nx < 0 or n <= nx or ny < 0 or m <= ny: continue
                if a[nx][ny] < 1 and not Visited[nx][ny]:
                    a[nx][ny] = -1
                    Visited[nx][ny] = True
                    tmpQueue.append([nx, ny])
        if not tmpQueue: break
        Queue = tmpQueue

T = 0
while True:
    T += 1
    fill(0, 0)
    cnt = 0
    for x in range(n):
        for y in range(m):
            if a[x][y] < 1: continue
            for dx, dy in drc:
                nx, ny = x + dx, y + dy
                if nx < 0 or n <= nx or ny < 0 or m <= ny: continue
                if a[nx][ny] == -1:
                    a[x][y] = 0
                    cnt += 1
                    ice -= 1
                    break
    if not ice:
        print(T, cnt)
        exit(0)