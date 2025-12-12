n = int(input())
arr = [0] + list(map(int, input().split())) + [0]

Left = [0] * (n + 2)
Right = [0] * (n + 2)

for i in range(1, n + 1): Left[i] = max(Left[i - 1], arr[i])
for i in range(n, 0, -1): Right[i] = max(Right[i + 1], arr[i])

Result = 0
for i in range(3, n - 1): Result = max(Result, Left[i - 2] + arr[i] + Right[i + 2])
print(Result)