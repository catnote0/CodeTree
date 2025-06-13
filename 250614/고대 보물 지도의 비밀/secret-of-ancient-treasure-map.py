n, k = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
inf = 0x7FFFFFFF

DP = [[-inf] * (n + 1) for _ in range(11)]
DP[0][0] = 0

for i in range(1, n + 1):
    num = numbers[i]
    if num >= 0: DP[0][i] = max(DP[0][i], DP[0][i - 1] + num, num)
    for j in range(1, 11):
        if num < 0: DP[j][i] = max(DP[j][i], DP[j - 1][i - 1] + num)
        else: DP[j][i] = max(DP[j][i], DP[j][i - 1] + num)

print(max(max(row) for row in DP[:k + 1]))