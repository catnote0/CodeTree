n = int(input())
Result = [1, 1, 3]
for i in range(3, n + 1): Result.append((Result[i - 2] * 2 + Result[i - 1]) % 10007)
print(Result[n])