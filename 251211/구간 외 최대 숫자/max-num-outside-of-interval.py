n, q = map(int, input().split())
arr = [0] + list(map(int, input().split())) + [0]
queries = [tuple(map(int, input().split())) for _ in range(q)]

Max_L = arr[:]
Max_R = arr[:]

for i in range(1, n + 1): Max_L[i] = max(Max_L[i - 1], Max_L[i])
for i in range(n, 0, -1): Max_R[i] = max(Max_R[i + 1], Max_R[i])

for a, b in queries: print(max(Max_L[a - 1], Max_R[b + 1]))