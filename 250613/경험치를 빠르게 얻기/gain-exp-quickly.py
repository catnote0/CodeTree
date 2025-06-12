n, m = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(n)]

Max_DP = 2000000

DP = [0] + [0x7FFFFFFF] * Max_DP

for e, t in quests:
    for i in range(m - 1, -1, -1): DP[i + e] = min(DP[i + e], DP[i] + t)

result = min(DP[m:])

print(-1 if result == 0x7FFFFFFF else result)