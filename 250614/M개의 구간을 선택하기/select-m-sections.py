N, M = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
inf = 0x7FFFFFFF

DP = [[-inf] * (2 * M + 1) for _ in range(N + 1)]
DP[0][0] = 0

for i in range(1, N + 1):
    for j in range(2 * M + 1):
        if j % 2 == 0: DP[i][j] = max(DP[i - 1][j - 1], DP[i - 1][j])
        else: DP[i][j] = max(DP[i - 1][j - 1], DP[i - 1][j]) + numbers[i]

print(max(DP[N][2 * M - 1], DP[N][2 * M]))