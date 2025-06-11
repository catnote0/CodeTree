n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]
result = 0

def BFS(x, y):
    Queue = [[x, y]]
    T = 0
    while True:
        T += 1
        tmpQueue = []
        for x, y in Queue:
            for dx, dy in drc:
                nx, ny = x + dx, y + dy
                if nx < 0 or n <= nx or ny < 0 or n <= ny: continue
                if grid[nx][ny] < grid[x][y]: tmpQueue.append([nx, ny])
        if not tmpQueue: return T
        Queue = tmpQueue

for x in range(n):
    for y in range(n):
        highest = True
        for dx, dy in drc:
            nx, ny = x + dx, y + dy
            if nx < 0 or n <= nx or ny < 0 or n <= ny: continue
            if grid[nx][ny] > grid[x][y]:
                highest = False
                break
        if highest: result = max(result, BFS(x, y))

print(result)