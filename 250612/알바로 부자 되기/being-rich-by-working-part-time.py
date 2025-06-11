n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0] * n
result = 0

for i in range(n):
    max_value = 0
    for j in range(i):
        if jobs[j][1] < jobs[i][0]: max_value = max(max_value, dp[j])
    dp[i] = max_value + jobs[i][2]
    result = max(result, dp[i])

print(result)