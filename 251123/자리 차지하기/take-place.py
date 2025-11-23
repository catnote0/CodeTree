from sortedcontainers import SortedSet

n, m = map(int, input().split())
a = list(map(int, input().split()))

S = SortedSet(range(1, m + 1))

for i, a_i in enumerate(a):
    opt = S.bisect_right(a_i) - 1
    if opt < 0:
        print(i)
        exit(0)
    S.remove(S[opt])

print(len(a))