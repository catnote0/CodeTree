n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
Visited = [[False] * n for _ in range(n)]
drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]
result = 0

def BFS(start_list):
    Queue = []
    for i in range(n):
        for j in range(n): Visited[i][j] = False
    for x, y in start_list:
        Queue.append([x, y])
        Visited[x][y] = True
    while True:
        tmpQueue = []
        for x, y in Queue:
            for dx, dy in drc:
                nx, ny = x + dx, y + dy
                if nx < 0 or n <= nx or ny < 0 or n <= ny: continue
                if u <= abs(grid[x][y] - grid[nx][ny]) <= d and not Visited[nx][ny]:
                    Visited[nx][ny] = True
                    tmpQueue.append([nx, ny])
        if not tmpQueue: break
        Queue = tmpQueue
    return sum(sum(1 if visit else 0 for visit in row) for row in Visited)

def select(num, cnt, start_list):
    global result
    if cnt == k:
        result = max(result, BFS(start_list))
        return
    if num == n * n: return
    select(num + 1, cnt + 1, start_list + [(num // n, num % n)])
    select(num + 1, cnt, start_list)

select(0, 0, [])
print(result)