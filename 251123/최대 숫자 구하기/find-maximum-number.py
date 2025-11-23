from sortedcontainers import SortedSet

n, m = map(int, input().split())
queries = list(map(int, input().split()))

S = SortedSet(range(1, m + 1))

for q in queries:
    S.remove(q)
    print(S[-1])