N = int(input())
B = [int(input()) for _ in range(N)]
A = [i for i in range(1, N * 2 + 1) if i not in B]

B.sort()
a = 0
Count = 0
for b in B:
    while a < N and A[a] < b: a += 1
    if a < N and A[a] > b:
        Count += 1
        a += 1

print(Count)