n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
Queue = [list(map(int, input().split())) for _ in range(k)]

for i in range(len(Queue)):
    Queue[i][0] -= 1
    Queue[i][1] -= 1
    grid[Queue[i][0]][Queue[i][1]] = -1

drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]
while True:
    tmpQueue = []
    for x, y in Queue:
        for dx, dy in drc:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if not grid[nx][ny]:
                grid[nx][ny] = -1
                tmpQueue.append([nx, ny])
    if not tmpQueue: break
    Queue = tmpQueue

print(sum(sum(1 if cell == -1 else 0 for cell in row) for row in grid))