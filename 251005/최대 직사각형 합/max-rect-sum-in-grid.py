N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(N): arr[i][j] += arr[i - 1][j]

Result = -0x7FFFFFFF
for i in range(N):
    for j in range(i, N):
        Sum = 0
        for k in range(N):
            row_sum = arr[j][k] - (arr[i - 1][k] if i > 0 else 0)
            Sum += row_sum
            if Result < Sum: Result = Sum
            if Sum < 0: Sum = 0

print(Result)