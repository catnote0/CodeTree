n, m = map(int, input().split())
arr = list(map(int, input().split()))

InnerCount = [0] * (m + 1)
OuterCount = [0] * (m + 1)
InnerUnique = 0
OuterUnique = 0

left = 0
right = -1

for num in arr:
    OuterCount[num] += 1
    if OuterCount[num] == 1: OuterUnique += 1

if OuterUnique < m or min(OuterCount[1:]) < 2:
    print(-1)
    exit(0)

Result = 0x7FFFFFFF
while True:
    if InnerUnique < m:
        right += 1
        if right == n: break
        InnerCount[arr[right]] += 1
        if InnerCount[arr[right]] == 1: InnerUnique += 1
        OuterCount[arr[right]] -= 1
        if OuterCount[arr[right]] == 0: OuterUnique -= 1
    else:
        Result = min(Result, right - left + 1)
        OuterCount[arr[left]] += 1
        if OuterCount[arr[left]] == 1: OuterUnique += 1
        InnerCount[arr[left]] -= 1
        if InnerCount[arr[left]] == 0: InnerUnique -= 1
        left += 1

print(-1 if Result == 0x7FFFFFFF else Result)
        