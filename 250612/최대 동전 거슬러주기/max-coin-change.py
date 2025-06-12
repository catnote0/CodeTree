N, M = map(int, input().split())
coin = list(map(int, input().split()))

DP = [0] + [-0x7FFFFFFF] * M

for c in coin:
    for i in range(M - c + 1): DP[i + c] = max(DP[i + c], DP[i] + 1)

print(-1 if DP[M] < 0 else DP[M])