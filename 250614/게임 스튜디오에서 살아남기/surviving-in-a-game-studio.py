n = int(input())
MOD = 1000000007

DP = [[[0] * 3 for _ in range(3)] for _ in range(n + 1)]
DP[0][0][0] = 1

for i in range(n):
    for j in range(3):
        for k in range(3):
            DP[i + 1][j][0] = (DP[i + 1][j][0] + DP[i][j][k]) % MOD
            if k + 1 < 3: DP[i + 1][j][k + 1] = (DP[i + 1][j][k + 1] + DP[i][j][k]) % MOD
            if j + 1 < 3: DP[i + 1][j + 1][0] = (DP[i + 1][j + 1][0] +  DP[i][j][k]) % MOD

print(sum(sum(row) for row in DP[n]) % MOD)