n = int(input())
m = list(map(int, input().split()))
dp = []
result = 0

for i in range(n):
    max_value = 0
    for j in range(i):
        if dp[j] > max_value and m[j] > m[i]: max_value = dp[j]
    dp.append(max_value + 1)
    result = max(result, dp[-1])

print(result)