n = int(input())
arr = list(map(int, input().split()))
last = 0
result = -1000

for i in range(n):
    if last < 0: last = arr[i]
    else: last += arr[i]
    result = max(result, last)

print(result)