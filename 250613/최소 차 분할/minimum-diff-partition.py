N = map(int, input().split())
coin = list(map(int, input().split()))
Sum = sum(coin)

DP = [0] + [0x7FFFFFFF] * Sum

for c in coin:
    for i in range(Sum - c, -1, -1): DP[i + c] = min(DP[i + c], DP[i] + 1)

result = 0x7FFFFFFF
for i in range(Sum + 1):
    if DP[i] != 0x7FFFFFFF: result = min(result, abs((Sum - i) - i))

print(result)