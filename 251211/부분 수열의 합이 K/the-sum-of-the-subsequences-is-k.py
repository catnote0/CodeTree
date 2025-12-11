n, k = map(int, input().split())
arr = list(map(int, input().split()))

Count = 0

for i in range(n):
    Sum = 0
    for j in range(i, n):
        Sum += arr[j]
        if Sum == k:
            Count += 1
            break

print(Count)