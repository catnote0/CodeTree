from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

S = SortedSet(arr)

Result = 0x7FFFFFFF
for num in arr:
    opt = S.bisect_left(num + m)
    if opt == len(S): continue
    Result = min(Result, S[opt] - num)

if Result == 0x7FFFFFFF: print(-1)
else: print(Result)