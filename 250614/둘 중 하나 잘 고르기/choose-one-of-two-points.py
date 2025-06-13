n = int(input())
red = [0]
blue = [0]

for _ in range(2 * n):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)

inf = 0x7FFFFFFF
DP = [[-inf] * (n * 2 + 1) for _ in range(n * 2 + 1)]
DP[0][n] = 0

for i in range(1, n * 2 + 1):
    for j in range(n * 2 + 1):
        if j > 0: DP[i][j] = max(DP[i][j], DP[i - 1][j - 1] + red[i])
        if j < n * 2: DP[i][j] = max(DP[i][j], DP[i - 1][j + 1] + blue[i])

print(DP[n * 2][n])