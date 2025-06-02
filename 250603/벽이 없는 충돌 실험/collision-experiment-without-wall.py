T = int(input())
drc = {'L': (-0.5, 0), 'R': (0.5, 0), 'U': (0, 0.5), 'D': (0, -0.5)}
BOUNDARY = 1100

for _ in range(T):
    N = int(input())
    x, y, w, d = [], [], [], []

    for i in range(N):
        xi, yi, wi, di = input().split()
        x.append(float(xi))
        y.append(float(yi))
        w.append(int(wi))
        d.append(di)

    live = [True] * N
    t = 0
    last_collide = -1

    while True:
        if not sum(live): break
        t += 1
        strong_bead = {}
        for i in range(N):
            if x[i] < -BOUNDARY or BOUNDARY < x[i] or y[i] < -BOUNDARY or BOUNDARY < y[i]: live[i] = False
            if not live[i]: continue
            x[i], y[i] = x[i] + drc[d[i]][0], y[i] + drc[d[i]][1]
            if (x[i], y[i]) in strong_bead:
                if strong_bead[(x[i], y[i])] > (w[i], i): live[i] = False
                else:
                    live[strong_bead[(x[i], y[i])][1]] = False
                    strong_bead[(x[i], y[i])] = (w[i], i)
                last_collide = t
            else: strong_bead[(x[i], y[i])] = (w[i], i)

    print(last_collide)