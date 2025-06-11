n = int(input())

# Please write your code here.
dp = [1, 2, 7]
for i in range(3, n + 1):
    Sum = 0
    for j in range(0, i - 2): Sum += dp[j]
    dp.append((Sum * 2 + dp[-2] * 3 + dp[-1] * 2) % 1000000007)

print(dp[n])
