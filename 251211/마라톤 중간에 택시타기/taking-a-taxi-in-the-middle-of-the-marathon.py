n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

Dist = []
Skip = [-1]
for i in range(n - 1): Dist.append(abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i]))
for i in range(1, n - 1): Skip.append(abs(x[i + 1] - x[i - 1]) + abs(y[i + 1] - y[i - 1]))

Sum_Dist = sum(Dist)

Result = 0x7FFFFFFF
for i in range(1, n - 1): Result = min(Result, Sum_Dist - Dist[i - 1] - Dist[i] + Skip[i])
print(Result)