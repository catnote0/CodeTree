n, m = map(int, input().split())

A = [input() for _ in range(n)]
B = [input() for _ in range(n)]

# Please write your code here.

Result = 0

for t1 in range(m):
    for t2 in range(t1 + 1, m):
        for t3 in range(t2 + 1, m):
            S = set()
            for i in range(n): S.add(A[i][t1] + A[i][t2] + A[i][t3])
            Overlap = False
            for i in range(n):
                if B[i][t1] + B[i][t2] + B[i][t3] in S:
                    Overlap = True
                    break
            if not Overlap: Result += 1

print(Result)