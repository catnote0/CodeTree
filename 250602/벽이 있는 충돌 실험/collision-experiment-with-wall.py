move = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    x, y, d = [], [], []
    live = [True] * M
    for _ in range(M):
        xi, yi, di = input().split()
        x.append(int(xi) - 1)
        y.append(int(yi) - 1)
        d.append(di)
    for _ in range(N * 3):
        check_grid = [[0] * N for _ in range(N)]
        for i in range(M):
            if not live[i]: continue
            if x[i] == 0 and d[i] == 'U': d[i] = 'D'
            elif x[i] == N - 1 and d[i] == 'D': d[i] = 'U'
            elif y[i] == 0 and d[i] == 'L': d[i] = 'R'
            elif y[i] == N - 1 and d[i] == 'R': d[i] = 'L'
            else: x[i], y[i] = x[i] + move[d[i]][0], y[i] + move[d[i]][1]
            check_grid[x[i]][y[i]] += 1
        for i in range(M):
            if check_grid[x[i]][y[i]] > 1: live[i] = False
    print(sum(live))