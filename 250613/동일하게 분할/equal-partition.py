N = map(int, input().split())
coin = list(map(int, input().split()))
Sum = sum(coin)

if Sum % 2 == 1:
    print("No")
    exit(0)

DP = [0] + [0x7FFFFFFF] * Sum

for c in coin:
    for i in range(Sum - c, -1, -1): DP[i + c] = min(DP[i + c], DP[i] + 1)

print("Yes" if DP[Sum // 2] < 0x7FFFFFFF else "No")