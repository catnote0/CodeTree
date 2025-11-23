from sortedcontainers import SortedSet

n, m = map(int, input().split())

# Store points as list of tuples (x, y)
points = [tuple(map(int, input().split())) for _ in range(n)]

# Store queries
queries = [int(input()) for _ in range(m)]

S = SortedSet(points)

for q in queries:
    opt = S.bisect_left((q, 0))
    if opt == len(S):
        print(-1, -1)
        continue
    else:
        x, y = S[opt]
        print(x, y)
        S.remove(S[opt])
