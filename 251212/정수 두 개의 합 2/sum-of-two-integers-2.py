n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()
right = n - 1

Sum = 0
for left in range(n):
    while left < right:
        if arr[left] + arr[right] <= k:
            Sum += (right - left)
            break
        right -= 1

print(Sum)