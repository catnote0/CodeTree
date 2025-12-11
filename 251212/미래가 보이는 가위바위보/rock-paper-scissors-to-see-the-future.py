N = int(input())
B = [input() for _ in range(N)]

Dict = {'H': 0, 'S': 1, 'P': 2}

Left = [[0] * 3 for _ in range(N)]
Right = [[0] * 3 for _ in range(N)]

Left[0][Dict[B[0]]] = 1
Right[N - 1][Dict[B[N - 1]]] = 1
for i in range(1, N):
    Left[i] = Left[i - 1][:]
    Left[i][Dict[B[i]]] += 1
for i in range(N - 2, -1, -1):
    Right[i] = Right[i + 1][:]
    Right[i][Dict[B[i]]] += 1

Result = 0
for i in range(N - 1): Result = max(Result, max(Left[i]) + max(Right[i + 1]))
print(Result)