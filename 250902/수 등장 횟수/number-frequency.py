n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

Count = {}
for n in arr: Count[n] = Count[n] + 1 if n in Count else 1
for q in nums: print(Count[q] if q in Count else 0, end = " ")