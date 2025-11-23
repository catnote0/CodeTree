from sortedcontainers import SortedSet

n, m = map(int, input().split())
sequence = list(map(int, input().split()))
query = list(map(int, input().split()))

S = SortedSet(sequence)

for q in query:
    opt = S.bisect_right(q) - 1
    if opt < 0:
        print(-1)
        continue
    print(S[opt])
    S.remove(S[opt])