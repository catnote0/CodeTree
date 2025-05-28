A = input()
result = len(A) * 2

for i in range(len(A)):
    combo = 1
    length = 0
    for j in range(len(A)):
        if j < len(A) - 1 and A[j] == A[j + 1]: combo += 1
        else:
            length += len(str(combo)) + 1
            combo = 1
    result = min(result, length)
    A = A[1:] + A[:1]

print(result)