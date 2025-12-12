import bisect

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

for q in queries: print(bisect.bisect_right(arr, q) - bisect.bisect_left(arr, q))