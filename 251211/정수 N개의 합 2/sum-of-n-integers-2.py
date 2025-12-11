n, k = map(int, input().split())
arr = list(map(int, input().split()))

Sum = 0

for i in range(k): Sum += arr[i]

Result = Sum

for i in range(k, n):
    Sum += (arr[i] - arr[i - k])
    Result = max(Result, Sum)

print(Result)