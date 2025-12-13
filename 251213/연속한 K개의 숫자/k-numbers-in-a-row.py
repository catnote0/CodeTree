N, K, B = map(int, input().split())
missing = set([int(input()) for _ in range(B)])

Result = 0x7FFFFFFF
Count = 0
for i in range(1, N + 1):
    if i in missing: Count += 1
    if (i - K) > 0 and (i - K) in missing: Count -= 1
    if i >= K: Result = min(Result, Count)

print(Result)