n = int(input())
coin = [0] + list(map(int, input().split()))

DP = [[0] * 4 for _ in range(n + 1)]
DP[1][1] = coin[1]

for i in range(2, n + 1):
    DP[i][0] = DP[i - 2][0] + coin[i]
    for j in range(1, 4): DP[i][j] = max(DP[i - 2][j], DP[i - 1][j - 1]) + coin[i]

print(max(DP[n]))