n = int(input())
profit = [0] + list(map(int, input().split()))

DP = [0]

for i in range(1, n + 1):
    Max = 0
    for j in range(i): Max = max(Max, DP[j] + profit[i - j])
    DP.append(Max)

print(DP[n])