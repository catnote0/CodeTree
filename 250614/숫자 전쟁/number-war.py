n = int(input())
first_cards = list(map(int, input().split()))
second_cards = list(map(int, input().split()))
inf = 0x7FFFFFFF

DP = [[-inf] * (n + 1) for _ in range(n + 1)]
DP[0][0] = 0

for i in range(n):
    for j in range(n):
        if DP[i][j] < 0: continue
        f, s = first_cards[i], second_cards[j]
        if f < s: DP[i + 1][j] = max(DP[i + 1][j], DP[i][j])
        if f > s: DP[i][j + 1] = max(DP[i][j + 1], DP[i][j] + s)
        DP[i + 1][j + 1] = max(DP[i + 1][j + 1], DP[i][j])

result = 0
for i in range(n): result = max(result, DP[i][n], DP[n][i])
print(result)