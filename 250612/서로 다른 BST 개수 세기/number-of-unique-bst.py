n = int(input())

dp = [1, 1, 2]

for i in range(3, n + 1):
    Sum = 0
    for j in range(0, i): Sum += (dp[j] * dp[i - j - 1])
    dp.append(Sum)

print(dp[n])