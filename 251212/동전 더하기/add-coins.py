n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

Count = 0
for i in range(n - 1, -1, -1):
    Count += k // coins[i]
    k %= coins[i]

print(Count)