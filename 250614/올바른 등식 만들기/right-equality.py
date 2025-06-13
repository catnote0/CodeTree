N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))
inf = 0x7FFFFFFF

DP = [[0] * 41 for _ in range(N + 1)]
DP[0][20] = 1

for i in range(1, N + 1):
    for j in range(41):
        if j - nums[i] >= 0: DP[i][j] += DP[i - 1][j - nums[i]]
        if j + nums[i] <= 40: DP[i][j] += DP[i - 1][j + nums[i]]

print(DP[N][20 + M])