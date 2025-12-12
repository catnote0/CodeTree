A = input()
n = len(A)

Right = [0] * n

for i in range(n - 2, -1, -1):
    Right[i] += Right[i + 1]
    if A[i + 1] == ')' and A[i] == ')': Right[i] += 1

Result = 0
for i in range(1, n - 1):
    if A[i - 1] == '(' and A[i] == '(': Result += Right[i + 1]

print(Result)