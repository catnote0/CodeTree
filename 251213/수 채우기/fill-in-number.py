import sys
sys.setrecursionlimit(100000)

inf = 0x7FFFFFFF
n = int(input())
ans = [inf, inf, 1, inf, 2, 1] + [inf] * n

def solve(n):
    if n < 0: return inf
    if ans[n] < inf: return ans[n]
    ans[n] = min(solve(n - 2), solve(n - 5)) + 1
    return ans[n]

Result = solve(n)
print(-1 if Result >= inf else Result)