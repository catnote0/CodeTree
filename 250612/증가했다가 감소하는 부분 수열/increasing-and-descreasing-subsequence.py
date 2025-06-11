n = int(input())
sequence = list(map(int, input().split()))
dp = [0] * n
dp_rev = [0] * n

for i in range(n):
    max_value = 0
    for j in range(i):
        if sequence[j] < sequence[i]: max_value = max(max_value, dp[j])
    dp[i] = max_value + 1

for i in range(n - 1, -1, -1):
    max_value = 0
    for j in range(n - 1, i, -1):
        if sequence[j] < sequence[i]: max_value = max(max_value, dp_rev[j])
    dp_rev[i] = max_value + 1

result = 0
for i in range(n): result = max(result, dp[i] + dp_rev[i] - 1)

print(result)
