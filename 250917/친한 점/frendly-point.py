from sortedcontainers import SortedSet

n, m = map(int, input().split())

# Store points as list of tuples
points = [tuple(map(int, input().split())) for _ in range(n)]

# Store queries as list of tuples
queries = [tuple(map(int, input().split())) for _ in range(m)]

SS = SortedSet(points)

for q in queries:
    pos = SS.bisect_left(q)
    if pos == len(SS): print("-1 -1")
    else: print(SS[pos][0], SS[pos][1])