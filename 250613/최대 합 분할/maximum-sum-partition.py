n = int(input())
arr = list(map(int, input().split()))
OFFSET = sum(arr)

DP = [-0x7FFFFFFF] * OFFSET + [0] + [-0x7FFFFFFF] * OFFSET

for num in arr:
    tmpDP = DP[:]
    for i in range(OFFSET * 2 + 1):
        if DP[i] < 0: continue
        sum_A, sum_B = 0, 0
        if i - OFFSET <= 0: sum_A, sum_B = DP[i], DP[i] - (i - OFFSET)
        else: sum_A, sum_B = DP[i] + (i - OFFSET), DP[i]
        tmpDP[(sum_A + num) - sum_B + OFFSET] = max(tmpDP[(sum_A + num) - sum_B + OFFSET], min(sum_A + num, sum_B))
        tmpDP[sum_A - (sum_B + num) + OFFSET] = max(tmpDP[sum_A - (sum_B + num) + OFFSET], min(sum_A, sum_B + num))
    DP = tmpDP[:]

print(DP[OFFSET])