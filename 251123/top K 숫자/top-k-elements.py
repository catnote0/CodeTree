from sortedcontainers import SortedSet

n, k = map(int, input().split())
arr = list(map(int, input().split()))

S = SortedSet()

for num in arr: S.add(num)

for i in range(1, k + 1): print(S[-i], end = " ")