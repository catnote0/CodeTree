N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

eff = [i / j for i, j in zip(v, w)]
jewels = []

for weight, value in zip(w, v):
    eff = value / weight
    jewels.append((eff, weight, value))

jewels.sort(key = lambda x: -x[0])

Sum = 0
Result = 0
for eff, weight, value in jewels:
    if M - Sum >= weight:
        Sum += weight
        Result += value
    else:
        Result += eff * (M - Sum)
        break

print("%.3f"%Result)