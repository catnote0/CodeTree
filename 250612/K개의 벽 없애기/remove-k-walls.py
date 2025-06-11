n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
MAX_DIST = 0x7FFFFFFF
Distance = [[MAX_DIST] * n for _ in range(n)]
drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]
wall = 0
wall_list = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            wall += 1
            wall_list.append([i, j])

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1
result = MAX_DIST

def BFS():
    for i in range(n):
        for j in range(n): Distance[i][j] = MAX_DIST
    Distance[r1][c1] = 0
    Queue = [[r1, c1]]
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
    return Distance[r2][c2]

def destroy(num, cnt):
    global result
    if cnt == k:
        result = min(result, BFS())
        return
    if num == wall: return
    x, y = wall_list[num]
    grid[x][y] = 0
    destroy(num + 1, cnt + 1)
    grid[x][y] = 1
    destroy(num + 1, cnt)

destroy(0, 0)
print(-1 if result == MAX_DIST else result)