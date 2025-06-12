N, M = map(int, input().split())
coin = list(map(int, input().split()))

DP = [0] * (M + 1)

for c in coin:
    for i in range(0, M - c + 1): DP[i + c] = max(DP[i + c], DP[i] + 1)

print(-1 if not DP[M] else DP[M])