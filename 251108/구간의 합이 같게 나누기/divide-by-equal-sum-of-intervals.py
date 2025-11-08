n = int(input())
arr = list(map(int, input().split()))

LeftSumCount = [0] * n
RightSumCount = [0] * n

Sum = sum(arr)
if Sum % 4 != 0:
    print("0")
    exit(0)

curr_sum = 0
for i, num in enumerate(arr):
    curr_sum += num
    if curr_sum == Sum // 4: LeftSumCount[i] += 1
    if i > 0: LeftSumCount[i] += LeftSumCount[i - 1]

curr_sum = 0
for i, num in enumerate(reversed(arr)):
    i = n - 1 - i
    curr_sum += num
    if curr_sum == Sum // 4: RightSumCount[i] += 1
    if i < n - 1: RightSumCount[i] += RightSumCount[i + 1]

Result = 0
curr_sum = 0
for i, num in enumerate(arr):
    curr_sum += num
    if curr_sum == Sum // 2 and i > 0 and i < n - 2: Result += LeftSumCount[i - 1] * RightSumCount[i + 2]

print(Result)