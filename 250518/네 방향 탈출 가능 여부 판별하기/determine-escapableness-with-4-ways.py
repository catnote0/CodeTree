n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dir4 = [[-1, 0], [0, -1], [0, 1], [1, 0]]
Queue = [[0, 0]]
a[0][0] = -1
while True:
    tmpQueue = []
    for pos in Queue:
        for d in dir4:
            (dx, dy) = (pos[0] + d[0], pos[1] + d[1])
            if dx < 0 or dx >= n or dy < 0 or dy >= m: continue
            if a[dx][dy] == 1:
                a[dx][dy] = -1
                tmpQueue.append([dx, dy])
    if not tmpQueue: break
    Queue = tmpQueue

print(1 if a[n - 1][m - 1] == -1 else 0)