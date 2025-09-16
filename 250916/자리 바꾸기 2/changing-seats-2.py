n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(k)]

Seat = [0]
SetArr = [0]

for i in range(1, n + 1):
    Seat.append(i)
    SetArr.append(set([i]))

for i in range(3):
    for a, b in edges:
        SetArr[Seat[a]].add(b)
        SetArr[Seat[b]].add(a)
        Seat[a], Seat[b] = Seat[b], Seat[a]

for i in range(1, n + 1): print(len(SetArr[i]))
