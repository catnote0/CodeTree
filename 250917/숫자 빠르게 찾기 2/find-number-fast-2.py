from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

SS = SortedSet(arr)

for q in queries:
    pos = SS.bisect_left(q)
    if pos == len(SS): print(-1)
    else: print(SS[pos])