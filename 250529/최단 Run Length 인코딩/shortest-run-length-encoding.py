from itertools import groupby
A = input()
print(min(sum(len(str(sum(1 for _ in grp))) + 1 for _, grp in groupby(A[i:] + A[:i])) for i in range(len(A))))