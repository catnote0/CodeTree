N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

DP = [0] + [-0x7FFFFFFF] * M

for i in range(N):
    for j in range(M - w[i], -1, -1):
        DP[j + w[i]] = max(DP[j + w[i]], DP[j] + v[i])

print(max(DP))