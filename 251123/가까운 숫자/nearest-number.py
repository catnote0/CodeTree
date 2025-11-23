from sortedcontainers import SortedSet

n = int(input())
queries = list(map(int, input().split()))

S = SortedSet([0])

Result = 0x7FFFFFFF
for q in queries:
    r = S.bisect_right(q)
    if r < len(S): Result = min(Result, S[r] - q)
    Result = min(Result, q - S[r - 1])
    S.add(q)
    print(Result)