n = int(input())
word = 'X' + input() + 'X'

Left_C = [0] * (n + 2)
Right_W = [0] * (n + 2)

for i in range(1, n + 1): Left_C[i] += (Left_C[i - 1] + (1 if word[i] == 'C' else 0))
for i in range(n, 0, -1): Right_W[i] += (Right_W[i + 1] + (1 if word[i] == 'W' else 0))

Result = 0
for i in range(2, n): Result += (1 if word[i] == 'O' else 0) * Left_C[i - 1] * Right_W[i + 1]
print(Result)