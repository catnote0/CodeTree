n, q = map(int, input().split())
points = list(map(int, input().split()))
ranges = [tuple(map(int, input().split())) for _ in range(q)]

Line = [0] * 1100000
for p in points: Line[p] = 1
for i in range(1, 1000000): Line[i] += Line[i - 1]

for a, b in ranges:
    if a == 0: print(Line[b])
    else: print(Line[b] - Line[a - 1])