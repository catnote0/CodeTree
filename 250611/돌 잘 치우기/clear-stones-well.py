n, k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

r = []
c = []
for _ in range(k):
    ri, ci = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)

stone = 0
stone_list = []
drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]
visited = [[False] * n for _ in range(n)]
result = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            stone_list.append((i, j))
            stone += 1

def BFS():
    for i in range(n):
        for j in range(n): visited[i][j] = False
    Queue = []
    for i in range(k):
        Queue.append([r[i], c[i]])
        visited[r[i]][c[i]] = True
    while True:
        tmpQueue = []
        for x, y in Queue:
            for dx, dy in drc:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                if not grid[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    tmpQueue.append([nx, ny])
        if not tmpQueue: break
        Queue = tmpQueue
    return sum(sum(1 if visit else 0 for visit in row) for row in visited)

def remove(num, cnt):
    global result
    if cnt == m:
        result = max(result, BFS())
        return
    if num == stone: return
    x, y = stone_list[num]
    grid[x][y] = 0
    remove(num + 1, cnt + 1)
    grid[x][y] = 1
    remove(num + 1, cnt)

remove(0, 0)
print(result)