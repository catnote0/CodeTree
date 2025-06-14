T = int(input())
drc = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
strong_bead = {}

for _ in range(T):
    N = int(input())
    x, y, w, d = [], [], [], []

    for i in range(N):
        xi, yi, wi, di = input().split()
        x.append(int(xi) * 2)
        y.append(int(yi) * 2)
        w.append(int(wi))
        d.append(di)
    live = [True] * N
    t = 0
    last_collide = -1
    alive_bead = N
    min_x, max_x, min_y, max_y = min(x), max(x), min(y), max(y)

    while True:
        if alive_bead <= 1: break
        t += 1
        strong_bead.clear()
        for i in range(N):
            if not live[i]: continue
            if x[i] < min_x or max_x < x[i] or y[i] < min_y or max_y < y[i]:
                live[i] = False
                alive_bead -= 1
                continue
            x[i], y[i] = x[i] + drc[d[i]][0], y[i] + drc[d[i]][1]
            pri = w[i] * 1000 + i;
            xy = x[i] * 10000 + y[i]
            if xy in strong_bead:
                now_pri = strong_bead[xy]
                if now_pri > pri: live[i] = False
                else:
                    live[now_pri % 1000] = False
                    strong_bead[xy] = pri
                last_collide = t
                alive_bead -= 1
            else: strong_bead[xy] = pri

    print(last_collide)